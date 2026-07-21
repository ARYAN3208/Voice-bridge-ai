const Settings = {

    defaults: {
        theme: "light",
        notifications: true,
        autoSave: true,
        autoPlay: false,
        language: "English"
    },

    init() {
        this.load();
        this.theme();
        this.notifications();
        this.autoSave();
        this.autoPlay();
        this.language();
        this.reset();
    },

    load() {

        const settings = JSON.parse(
            localStorage.getItem("settings")
        ) || this.defaults;

        document.body.classList.toggle(
            "dark",
            settings.theme === "dark"
        );

        this.checked("notificationSwitch", settings.notifications);
        this.checked("autoSaveSwitch", settings.autoSave);
        this.checked("autoPlaySwitch", settings.autoPlay);

        const language = document.getElementById("languageSelect");

        if (language) {
            language.value = settings.language;
        }

    },

    save(key, value) {

        const settings = JSON.parse(
            localStorage.getItem("settings")
        ) || this.defaults;

        settings[key] = value;

        localStorage.setItem(
            "settings",
            JSON.stringify(settings)
        );

    },

    checked(id, value) {

        const element = document.getElementById(id);

        if (!element) return;

        if (value) {
            element.classList.add("active");
        } else {
            element.classList.remove("active");
        }

    },

    toggle(id, key) {

        const element = document.getElementById(id);

        if (!element) return;

        element.addEventListener("click", () => {

            element.classList.toggle("active");

            const enabled = element.classList.contains("active");

            this.save(key, enabled);

            showToast(
                "Settings",
                `${key} ${enabled ? "enabled" : "disabled"}`
            );

        });

    },

    theme() {

        const button = document.getElementById("themeSwitch");

        if (!button) return;

        button.addEventListener("click", () => {

            button.classList.toggle("active");

            const dark = button.classList.contains("active");

            document.body.classList.toggle("dark", dark);

            this.save(
                "theme",
                dark ? "dark" : "light"
            );

            showToast(
                "Theme",
                dark
                    ? "Dark mode enabled"
                    : "Light mode enabled"
            );

        });

    },

    notifications() {

        this.toggle(
            "notificationSwitch",
            "notifications"
        );

    },

    autoSave() {

        this.toggle(
            "autoSaveSwitch",
            "autoSave"
        );

    },

    autoPlay() {

        this.toggle(
            "autoPlaySwitch",
            "autoPlay"
        );

    },

    language() {

        const select = document.getElementById("languageSelect");

        if (!select) return;

        select.addEventListener("change", () => {

            this.save(
                "language",
                select.value
            );

            showToast(
                "Language",
                `${select.value} selected`
            );

        });

    },

    reset() {

        const button = document.getElementById("resetSettings");

        if (!button) return;

        button.addEventListener("click", () => {

            localStorage.setItem(
                "settings",
                JSON.stringify(this.defaults)
            );

            showToast(
                "Settings",
                "Settings restored."
            );

            setTimeout(() => {

                location.reload();

            }, 1000);

        });

    }

};

document.addEventListener("DOMContentLoaded", () => {

    Settings.init();

});