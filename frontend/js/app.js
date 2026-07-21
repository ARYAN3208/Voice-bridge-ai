const App = {

    init() {
        this.sidebar();
        this.dropdown();
        this.modal();
        this.toast();
        this.scrollTop();
        this.activeNav();
        this.smoothScroll();
    },

    sidebar() {

        const toggle = document.querySelector(".sidebar-toggle");
        const sidebar = document.querySelector(".sidebar");

        if (!toggle || !sidebar) return;

        toggle.addEventListener("click", () => {
            sidebar.classList.toggle("collapsed");
        });

    },

    dropdown() {

        const dropdowns = document.querySelectorAll(".dropdown");

        dropdowns.forEach(dropdown => {

            const button = dropdown.querySelector(".dropdown-toggle");

            if (!button) return;

            button.addEventListener("click", e => {

                e.stopPropagation();

                dropdown.classList.toggle("open");

            });

        });

        document.addEventListener("click", () => {

            dropdowns.forEach(dropdown => {

                dropdown.classList.remove("open");

            });

        });

    },

    modal() {

        const openButtons = document.querySelectorAll("[data-modal]");

        const closeButtons = document.querySelectorAll(".modal-close");

        openButtons.forEach(button => {

            button.addEventListener("click", () => {

                const id = button.dataset.modal;

                const modal = document.getElementById(id);

                if (modal) {

                    modal.classList.add("show");

                }

            });

        });

        closeButtons.forEach(button => {

            button.addEventListener("click", () => {

                button.closest(".modal").classList.remove("show");

            });

        });

        window.addEventListener("click", e => {

            if (e.target.classList.contains("modal")) {

                e.target.classList.remove("show");

            }

        });

    },

    toast() {

        window.showToast = function (title, message) {

            const toast = document.createElement("div");

            toast.className = "toast";

            toast.innerHTML = `
                <div class="toast-title">${title}</div>
                <div class="toast-text">${message}</div>
            `;

            document.body.appendChild(toast);

            setTimeout(() => {

                toast.remove();

            }, 3000);

        };

    },

    activeNav() {

        const links = document.querySelectorAll(".nav-links a");

        const current = window.location.pathname.split("/").pop();

        links.forEach(link => {

            if (link.getAttribute("href") === current) {

                link.classList.add("active");

            }

        });

    },

    smoothScroll() {

        document.querySelectorAll('a[href^="#"]').forEach(anchor => {

            anchor.addEventListener("click", function (e) {

                e.preventDefault();

                const target = document.querySelector(this.getAttribute("href"));

                if (target) {

                    target.scrollIntoView({

                        behavior: "smooth"

                    });

                }

            });

        });

    },

    scrollTop() {

        const button = document.querySelector(".scroll-top");

        if (!button) return;

        window.addEventListener("scroll", () => {

            button.classList.toggle("show", window.scrollY > 300);

        });

        button.addEventListener("click", () => {

            window.scrollTo({

                top: 0,

                behavior: "smooth"

            });

        });

    }

};

document.addEventListener("DOMContentLoaded", () => {

    App.init();

});