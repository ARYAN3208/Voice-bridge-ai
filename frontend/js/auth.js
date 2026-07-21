const Auth = {

    init() {
        this.passwordToggle();
        this.login();
        this.register();
        this.forgotPassword();
        this.passwordStrength();
    },

    passwordToggle() {

        const toggles = document.querySelectorAll("[data-password-toggle]");

        toggles.forEach(toggle => {

            toggle.addEventListener("click", () => {

                const input = document.getElementById(toggle.dataset.passwordToggle);

                if (!input) return;

                const visible = input.type === "text";

                input.type = visible ? "password" : "text";

                toggle.innerHTML = visible
                    ? '<i class="fa-regular fa-eye"></i>'
                    : '<i class="fa-regular fa-eye-slash"></i>';

            });

        });

    },

    login() {

        const form = document.getElementById("loginForm");

        if (!form) return;

        form.addEventListener("submit", e => {

            e.preventDefault();

            const email = form.email.value.trim();
            const password = form.password.value.trim();

            if (!email || !password) {

                showToast("Error", "Please fill all fields.");

                return;

            }

            showToast("Success", "Login successful.");

            setTimeout(() => {

                window.location.href = "dashboard.html";

            }, 1200);

        });

    },

    register() {

        const form = document.getElementById("registerForm");

        if (!form) return;

        form.addEventListener("submit", e => {

            e.preventDefault();

            const name = form.name.value.trim();
            const email = form.email.value.trim();
            const password = form.password.value.trim();
            const confirm = form.confirmPassword.value.trim();

            if (!name || !email || !password || !confirm) {

                showToast("Error", "Please fill all fields.");

                return;

            }

            if (password !== confirm) {

                showToast("Error", "Passwords do not match.");

                return;

            }

            showToast("Success", "Account created successfully.");

            setTimeout(() => {

                window.location.href = "login.html";

            }, 1500);

        });

    },

    forgotPassword() {

        const form = document.getElementById("forgotForm");

        if (!form) return;

        form.addEventListener("submit", e => {

            e.preventDefault();

            const email = form.email.value.trim();

            if (!email) {

                showToast("Error", "Enter your email.");

                return;

            }

            showToast("Success", "Password reset link sent.");

            form.reset();

        });

    },

    passwordStrength() {

        const input = document.getElementById("password");

        const strength = document.getElementById("passwordStrength");

        if (!input || !strength) return;

        input.addEventListener("input", () => {

            const value = input.value;

            let score = 0;

            if (value.length >= 8) score++;
            if (/[A-Z]/.test(value)) score++;
            if (/[0-9]/.test(value)) score++;
            if (/[^A-Za-z0-9]/.test(value)) score++;

            const levels = [
                "Very Weak",
                "Weak",
                "Medium",
                "Strong",
                "Very Strong"
            ];

            const colors = [
                "#EF4444",
                "#F97316",
                "#EAB308",
                "#22C55E",
                "#16A34A"
            ];

            strength.textContent = levels[score];
            strength.style.color = colors[score];

        });

    }

};

document.addEventListener("DOMContentLoaded", () => {

    Auth.init();

});