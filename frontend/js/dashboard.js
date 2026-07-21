const Dashboard = {

    init() {
        this.welcome();
        this.animateStats();
        this.search();
        this.quickActions();
        this.recentActivity();
        this.notification();
    },

    welcome() {

        const user = localStorage.getItem("username") || "Guest";

        const heading = document.getElementById("welcomeUser");

        if (heading) {
            heading.textContent = `Welcome back, ${user}`;
        }

    },

    animateStats() {

        const stats = document.querySelectorAll("[data-stat]");

        stats.forEach(stat => {

            const target = Number(stat.dataset.stat);

            let value = 0;

            const increment = Math.ceil(target / 100);

            const timer = setInterval(() => {

                value += increment;

                if (value >= target) {

                    value = target;

                    clearInterval(timer);

                }

                stat.textContent = value.toLocaleString();

            }, 15);

        });

    },

    search() {

        const input = document.getElementById("dashboardSearch");

        if (!input) return;

        input.addEventListener("keyup", () => {

            const keyword = input.value.toLowerCase();

            const cards = document.querySelectorAll(".dashboard-card");

            cards.forEach(card => {

                const text = card.textContent.toLowerCase();

                card.style.display = text.includes(keyword)
                    ? "block"
                    : "none";

            });

        });

    },

    quickActions() {

        const buttons = document.querySelectorAll("[data-action]");

        buttons.forEach(button => {

            button.addEventListener("click", () => {

                const action = button.dataset.action;

                switch (action) {

                    case "translate":
                        window.location.href = "translation.html";
                        break;

                    case "upload":
                        window.location.href = "voice-notes.html";
                        break;

                    case "history":
                        window.location.href = "history.html";
                        break;

                    case "profile":
                        window.location.href = "profile.html";
                        break;

                    default:
                        showToast("Info", "Feature coming soon.");

                }

            });

        });

    },

    recentActivity() {

        const list = document.getElementById("recentActivity");

        if (!list) return;

        const activities = [

            "Translated English → Hindi",

            "Uploaded Voice Note",

            "Downloaded Tamil Audio",

            "Updated Profile",

            "Started Live Translation"

        ];

        list.innerHTML = "";

        activities.forEach(activity => {

            const item = document.createElement("li");

            item.className = "activity-item";

            item.innerHTML = `
                <span>${activity}</span>
                <small>${this.time()}</small>
            `;

            list.appendChild(item);

        });

    },

    notification() {

        const button = document.getElementById("notify");

        if (!button) return;

        button.addEventListener("click", () => {

            showToast(
                "VoiceBridge AI",
                "No new notifications."
            );

        });

    },

    time() {

        const now = new Date();

        return now.toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit"
        });

    }

};

document.addEventListener("DOMContentLoaded", () => {

    Dashboard.init();

});