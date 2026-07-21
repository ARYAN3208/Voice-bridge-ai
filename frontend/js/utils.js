const Utils = {

    formatDate(date = new Date()) {

        return new Intl.DateTimeFormat("en-IN", {
            day: "2-digit",
            month: "short",
            year: "numeric"
        }).format(date);

    },

    formatTime(date = new Date()) {

        return new Intl.DateTimeFormat("en-IN", {
            hour: "2-digit",
            minute: "2-digit",
            hour12: true
        }).format(date);

    },

    formatDateTime(date = new Date()) {

        return `${this.formatDate(date)} ${this.formatTime(date)}`;

    },

    generateId(length = 12) {

        const chars =
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

        let id = "";

        for (let i = 0; i < length; i++) {

            id += chars.charAt(
                Math.floor(Math.random() * chars.length)
            );

        }

        return id;

    },

    debounce(callback, delay = 300) {

        let timer;

        return (...args) => {

            clearTimeout(timer);

            timer = setTimeout(() => {

                callback(...args);

            }, delay);

        };

    },

    throttle(callback, limit = 200) {

        let waiting = false;

        return (...args) => {

            if (waiting) return;

            callback(...args);

            waiting = true;

            setTimeout(() => {

                waiting = false;

            }, limit);

        };

    },

    show(element) {

        if (!element) return;

        element.style.display = "";

    },

    hide(element) {

        if (!element) return;

        element.style.display = "none";

    },

    toggle(element) {

        if (!element) return;

        const hidden = getComputedStyle(element).display === "none";

        element.style.display = hidden ? "" : "none";

    },

    copy(text) {

        navigator.clipboard.writeText(text);

        showToast(
            "Copied",
            "Copied to clipboard."
        );

    },

    download(filename, content, type = "text/plain") {

        const blob = new Blob(
            [content],
            {
                type
            }
        );

        const url = URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download = filename;

        link.click();

        URL.revokeObjectURL(url);

    },

    save(key, value) {

        localStorage.setItem(
            key,
            JSON.stringify(value)
        );

    },

    get(key) {

        const value = localStorage.getItem(key);

        return value ? JSON.parse(value) : null;

    },

    remove(key) {

        localStorage.removeItem(key);

    },

    clear() {

        localStorage.clear();

    },

    capitalize(text) {

        if (!text) return "";

        return text.charAt(0).toUpperCase() + text.slice(1);

    },

    truncate(text, length = 50) {

        if (text.length <= length) {

            return text;

        }

        return text.substring(0, length) + "...";

    },

    loading(button, state = true) {

        if (!button) return;

        if (state) {

            button.dataset.text = button.innerHTML;

            button.disabled = true;

            button.innerHTML = `
                <span class="loader"></span>
            `;

        } else {

            button.disabled = false;

            button.innerHTML = button.dataset.text;

        }

    },

    sleep(ms) {

        return new Promise(resolve => {

            setTimeout(resolve, ms);

        });

    },

    random(min, max) {

        return Math.floor(

            Math.random() * (max - min + 1)

        ) + min;

    },

    uuid() {

        return crypto.randomUUID();

    },

    isEmail(email) {

        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

    },

    isEmpty(value) {

        return value.trim().length === 0;

    }

};