const Animation = {

    init() {
        this.fadeIn();
        this.slideUp();
        this.counters();
        this.progress();
        this.hoverCards();
        this.parallax();
    },

    fadeIn() {

        const elements = document.querySelectorAll(".fade-in");

        if (!elements.length) return;

        const observer = new IntersectionObserver(entries => {

            entries.forEach(entry => {

                if (!entry.isIntersecting) return;

                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";

                observer.unobserve(entry.target);

            });

        }, {
            threshold: .15
        });

        elements.forEach(element => {

            element.style.opacity = "0";
            element.style.transform = "translateY(30px)";
            element.style.transition = ".6s ease";

            observer.observe(element);

        });

    },

    slideUp() {

        const elements = document.querySelectorAll(".slide-up");

        if (!elements.length) return;

        const observer = new IntersectionObserver(entries => {

            entries.forEach(entry => {

                if (!entry.isIntersecting) return;

                entry.target.classList.add("show");

                observer.unobserve(entry.target);

            });

        });

        elements.forEach(element => observer.observe(element));

    },

    counters() {

        const counters = document.querySelectorAll("[data-count]");

        if (!counters.length) return;

        counters.forEach(counter => {

            const target = Number(counter.dataset.count);

            let current = 0;

            const step = Math.ceil(target / 80);

            const timer = setInterval(() => {

                current += step;

                if (current >= target) {

                    current = target;

                    clearInterval(timer);

                }

                counter.textContent = current.toLocaleString();

            }, 20);

        });

    },

    progress() {

        const bars = document.querySelectorAll(".progress span");

        bars.forEach(bar => {

            const value = bar.dataset.progress || "0";

            requestAnimationFrame(() => {

                bar.style.width = value + "%";

            });

        });

    },

    hoverCards() {

        const cards = document.querySelectorAll(".card");

        cards.forEach(card => {

            card.addEventListener("mousemove", e => {

                const rect = card.getBoundingClientRect();

                const x = e.clientX - rect.left;

                const y = e.clientY - rect.top;

                const rotateX = ((y / rect.height) - .5) * -6;
                const rotateY = ((x / rect.width) - .5) * 6;

                card.style.transform =
                    `perspective(900px)
                     rotateX(${rotateX}deg)
                     rotateY(${rotateY}deg)
                     translateY(-6px)`;

            });

            card.addEventListener("mouseleave", () => {

                card.style.transform = "";

            });

        });

    },

    parallax() {

        const hero = document.querySelector(".hero-image");

        if (!hero) return;

        window.addEventListener("mousemove", e => {

            const x = (window.innerWidth / 2 - e.clientX) / 40;

            const y = (window.innerHeight / 2 - e.clientY) / 40;

            hero.style.transform = `translate(${x}px, ${y}px)`;

        });

    }

};

document.addEventListener("DOMContentLoaded", () => {

    Animation.init();

});