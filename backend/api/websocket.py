import asyncio
import json
from typing import Dict

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from deepgram import (
    DeepgramClient,
    LiveOptions,
    LiveTranscriptionEvents,
)

from config.settings import settings

router = APIRouter(
    prefix="/ws",
    tags=["WebSocket"],
)


class ConnectionManager:

    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(
        self,
        websocket: WebSocket,
        client_id: str,
    ):
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(
        self,
        client_id: str,
    ):
        self.active_connections.pop(client_id, None)

    async def send_json(
        self,
        client_id: str,
        data: dict,
    ):
        websocket = self.active_connections.get(client_id)

        if websocket:
            await websocket.send_json(data)


manager = ConnectionManager()

deepgram = DeepgramClient(settings.DEEPGRAM_API_KEY)

class LiveTranslator:

    def __init__(self):

        self.connection = None
        self.client_id = None

    async def start(
        self,
        client_id: str,
    ):

        self.client_id = client_id

        self.connection = deepgram.listen.websocket.v("1")

        self.connection.on(
            LiveTranscriptionEvents.Transcript,
            self.on_transcript,
        )

        options = LiveOptions(
            model="nova-3",
            language="multi",
            smart_format=True,
            punctuate=True,
            interim_results=True,
            diarize=True,
        )

        self.connection.start(options)

    async def send_audio(
        self,
        chunk: bytes,
    ):

        if self.connection:
            self.connection.send(chunk)

    async def close(self):

        if self.connection:
            self.connection.finish()

    async def on_transcript(
        self,
        self_,
        result,
        **kwargs,
    ):

        if not result.channel.alternatives:
            return

        transcript = (
            result.channel
            .alternatives[0]
            .transcript
        )

        if not transcript:
            return

        await manager.send_json(
            self.client_id,
            {
                "type": "transcript",
                "text": transcript,
                "is_final": result.is_final,
            },
        )

@router.websocket("/{client_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    client_id: str,
):

    await manager.connect(
        websocket,
        client_id,
    )

    translator = LiveTranslator()

    await translator.start(client_id)

    try:

        while True:

            audio = await websocket.receive_bytes()

            await translator.send_audio(audio)

    except WebSocketDisconnect:

        manager.disconnect(client_id)

        await translator.close()

    except Exception:

        manager.disconnect(client_id)

        await translator.close()