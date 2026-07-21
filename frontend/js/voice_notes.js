const VoiceNotes = {

    state: {
        recording: false,
        seconds: 0,
        timer: null,
        audio: null
    },

    init() {
        this.record();
        this.upload();
        this.dragDrop();
        this.audioPlayer();
        this.download();
        this.delete();
    },

    record() {

        const button = document.getElementById("recordVoice");
        const timer = document.getElementById("recordTimer");

        if (!button) return;

        button.addEventListener("click", () => {

            this.state.recording = !this.state.recording;

            button.classList.toggle("recording");

            if (this.state.recording) {

                button.innerHTML =
                    '<i class="fa-solid fa-stop"></i>';

                this.startTimer(timer);

                showToast(
                    "Recorder",
                    "Recording started."
                );

            } else {

                button.innerHTML =
                    '<i class="fa-solid fa-microphone"></i>';

                clearInterval(this.state.timer);

                showToast(
                    "Recorder",
                    "Recording stopped."
                );

            }

        });

    },

    startTimer(timer) {

        this.state.seconds = 0;

        timer.textContent = "00:00";

        this.state.timer = setInterval(() => {

            this.state.seconds++;

            const min = String(
                Math.floor(this.state.seconds / 60)
            ).padStart(2, "0");

            const sec = String(
                this.state.seconds % 60
            ).padStart(2, "0");

            timer.textContent = `${min}:${sec}`;

        }, 1000);

    },

    upload() {

        const input = document.getElementById("voiceUpload");

        if (!input) return;

        input.addEventListener("change", e => {

            const file = e.target.files[0];

            if (!file) return;

            showToast(
                "Upload",
                `${file.name} uploaded successfully.`
            );

        });

    },

    dragDrop() {

        const area = document.getElementById("dropArea");

        if (!area) return;

        area.addEventListener("dragover", e => {

            e.preventDefault();

            area.classList.add("dragging");

        });

        area.addEventListener("dragleave", () => {

            area.classList.remove("dragging");

        });

        area.addEventListener("drop", e => {

            e.preventDefault();

            area.classList.remove("dragging");

            const file = e.dataTransfer.files[0];

            if (!file) return;

            showToast(
                "Upload",
                `${file.name} uploaded successfully.`
            );

        });

    },

    audioPlayer() {

        const audio = document.getElementById("voicePlayer");

        const play = document.getElementById("playVoice");

        if (!audio || !play) return;

        play.addEventListener("click", () => {

            if (audio.paused) {

                audio.play();

                play.innerHTML =
                    '<i class="fa-solid fa-pause"></i>';

            } else {

                audio.pause();

                play.innerHTML =
                    '<i class="fa-solid fa-play"></i>';

            }

        });

        audio.addEventListener("ended", () => {

            play.innerHTML =
                '<i class="fa-solid fa-play"></i>';

        });

    },

    download() {

        document.querySelectorAll(".downloadVoice").forEach(button => {

            button.addEventListener("click", () => {

                showToast(
                    "Download",
                    "Voice note downloaded."
                );

            });

        });

    },

    delete() {

        document.querySelectorAll(".deleteVoice").forEach(button => {

            button.addEventListener("click", () => {

                const card = button.closest(".voice-card");

                if (card) {

                    card.remove();

                }

                showToast(
                    "Voice Notes",
                    "Voice note deleted."
                );

            });

        });

    }

};

document.addEventListener("DOMContentLoaded", () => {

    VoiceNotes.init();

});