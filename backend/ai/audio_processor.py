from pathlib import Path

from pydub import AudioSegment
from pydub.silence import split_on_silence

from backend.utils.constants import SUPPORTED_AUDIO_FORMATS


class AudioProcessor:
    def validate_audio(self, file_path: str) -> bool:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{file_path} not found.")

        if path.suffix.lower() not in SUPPORTED_AUDIO_FORMATS:
            raise ValueError("Unsupported audio format.")

        return True

    def load_audio(self, file_path: str) -> AudioSegment:
        self.validate_audio(file_path)
        return AudioSegment.from_file(file_path)

    def convert_to_wav(
        self,
        input_path: str,
        output_path: str,
    ) -> str:
        audio = self.load_audio(input_path)

        audio.export(
            output_path,
            format="wav",
        )

        return output_path

    def normalize_audio(
        self,
        input_path: str,
        output_path: str,
    ) -> str:
        audio = self.load_audio(input_path)

        normalized = audio.normalize()

        normalized.export(
            output_path,
            format="wav",
        )

        return output_path

    def resample_audio(
        self,
        input_path: str,
        output_path: str,
        sample_rate: int = 16000,
    ) -> str:
        audio = self.load_audio(input_path)

        audio = audio.set_frame_rate(sample_rate)
        audio = audio.set_channels(1)

        audio.export(
            output_path,
            format="wav",
        )

        return output_path

    def trim_silence(
        self,
        input_path: str,
        output_path: str,
    ) -> str:
        audio = self.load_audio(input_path)

        chunks = split_on_silence(
            audio,
            min_silence_len=500,
            silence_thresh=audio.dBFS - 14,
            keep_silence=200,
        )

        if not chunks:
            audio.export(output_path, format="wav")
            return output_path

        combined = AudioSegment.empty()

        for chunk in chunks:
            combined += chunk

        combined.export(
            output_path,
            format="wav",
        )

        return output_path

    def get_duration(self, file_path: str) -> float:
        audio = self.load_audio(file_path)
        return round(len(audio) / 1000, 2)


audio_processor = AudioProcessor()