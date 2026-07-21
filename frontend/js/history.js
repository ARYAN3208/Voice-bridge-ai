const History = {

    records: [],

    init() {
        this.load();
        this.search();
        this.filter();
        this.sort();
        this.clear();
        this.download();
    },

    load() {

        this.records = [

            {
                id: 1,
                source: "English",
                target: "Hindi",
                date: "2026-07-06",
                type: "Voice Note"
            },

            {
                id: 2,
                source: "Marathi",
                target: "Tamil",
                date: "2026-07-05",
                type: "Live"
            },

            {
                id: 3,
                source: "Hindi",
                target: "Gujarati",
                date: "2026-07-04",
                type: "Voice Note"
            }

        ];

    },

    search() {

        const input = document.getElementById("historySearch");

        if (!input) return;

        input.addEventListener("keyup", () => {

            const keyword = input.value.toLowerCase();

            document.querySelectorAll(".history-row").forEach(row => {

                const text = row.textContent.toLowerCase();

                row.style.display = text.includes(keyword)
                    ? ""
                    : "none";

            });

        });

    },

    filter() {

        const filter = document.getElementById("historyFilter");

        if (!filter) return;

        filter.addEventListener("change", () => {

            const value = filter.value;

            document.querySelectorAll(".history-row").forEach(row => {

                if (value === "All") {

                    row.style.display = "";

                    return;

                }

                row.style.display =
                    row.dataset.type === value
                        ? ""
                        : "none";

            });

        });

    },

    sort() {

        const sort = document.getElementById("historySort");

        if (!sort) return;

        sort.addEventListener("change", () => {

            showToast(
                "History",
                `Sorted by ${sort.value}`
            );

        });

    },

    clear() {

        const button = document.getElementById("clearHistory");

        if (!button) return;

        button.addEventListener("click", () => {

            const rows = document.querySelectorAll(".history-row");

            rows.forEach(row => row.remove());

            showToast(
                "History",
                "History cleared."
            );

        });

    },

    download() {

        document.querySelectorAll(".download-history").forEach(button => {

            button.addEventListener("click", () => {

                showToast(
                    "Download",
                    "Translation downloaded."
                );

            });

        });

    }

};

document.addEventListener("DOMContentLoaded", () => {

    History.init();

});