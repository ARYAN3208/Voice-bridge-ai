const Translation = {

    state: {
        recording: false,
        sourceLanguage: "English",
        targetLanguage: "Hindi",
        transcript: "",
        translation: ""
    },

    init() {
        this.record();
        this.language();
        this.swap();
        this.translate();
        this.copy();
        this.download();
        this.clear();
    },

    record() {

        const button = document.getElementById("recordButton");

        if (!button) return;

        button.addEventListener("click", () => {

            this.state.recording = !this.state.recording;

            button.classList.toggle("recording");

            button.innerHTML = this.state.recording
                ? '<i class="fa-solid fa-stop"></i>'
                : '<i class="fa-solid fa-microphone"></i>';

            showToast(
                "Recorder",
                this.state.recording
                    ? "Recording started."
                    : "Recording stopped."
            );

        });

    },

    language() {

        const source = document.getElementById("sourceLanguage");
        const target = document.getElementById("targetLanguage");

        if (source) {

            source.addEventListener("change", () => {

                this.state.sourceLanguage = source.value;

            });

        }

        if (target) {

            target.addEventListener("change", () => {

                this.state.targetLanguage = target.value;

            });

        }

    },

    swap() {

        const button = document.getElementById("swapLanguage");

        if (!button) return;

        button.addEventListener("click", () => {

            const source = document.getElementById("sourceLanguage");
            const target = document.getElementById("targetLanguage");

            if (!source || !target) return;

            const value = source.value;

            source.value = target.value;
            target.value = value;

            this.state.sourceLanguage = source.value;
            this.state.targetLanguage = target.value;

            showToast(
                "Languages",
                "Languages swapped."
            );

        });

    },

    translate() {

        const button = document.getElementById("translateButton");

        if (!button) return;

        button.addEventListener("click", () => {

            const transcript = document.getElementById("transcript");
            const output = document.getElementById("translationOutput");

            if (!transcript || !output) return;

            if (!transcript.value.trim()) {

                showToast(
                    "Translation",
                    "Please enter or record some text."
                );

                return;

            }

            this.state.transcript = transcript.value;

            output.value = `Translated (${this.state.targetLanguage}): ${transcript.value}`;

            this.state.translation = output.value;

            showToast(
                "Success",
                "Translation completed."
            );

        });

    },

    copy() {

        const button = document.getElementById("copyTranslation");

        if (!button) return;

        button.addEventListener("click", async () => {

            const output = document.getElementById("translationOutput");

            if (!output || !output.value) return;

            await navigator.clipboard.writeText(output.value);

            showToast(
                "Copied",
                "Translation copied."
            );

        });

    },

    download() {

        const button = document.getElementById("downloadTranslation");

        if (!button) return;

        button.addEventListener("click", () => {

            const output = document.getElementById("translationOutput");

            if (!output || !output.value) return;

            const blob = new Blob(
                [output.value],
                { type: "text/plain" }
            );

            const url = URL.createObjectURL(blob);

            const link = document.createElement("a");

            link.href = url;
            link.download = "translation.txt";

            link.click();

            URL.revokeObjectURL(url);

            showToast(
                "Download",
                "Translation downloaded."
            );

        });

    },

    clear() {

        const button = document.getElementById("clearTranslation");

        if (!button) return;

        button.addEventListener("click", () => {

            const transcript = document.getElementById("transcript");
            const output = document.getElementById("translationOutput");

            if (transcript) transcript.value = "";

            if (output) output.value = "";

            this.state.transcript = "";
            this.state.translation = "";

            showToast(
                "Translation",
                "Workspace cleared."
            );

        });

    }

};

document.addEventListener("DOMContentLoaded", () => {

    Translation.init();

});