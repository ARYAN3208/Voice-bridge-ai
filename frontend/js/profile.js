const Profile = {

    init() {
        this.avatar();
        this.profileForm();
        this.passwordForm();
        this.theme();
        this.logout();
    },

    avatar() {

        const input = document.getElementById("avatarInput");
        const preview = document.getElementById("profileAvatar");

        if (!input || !preview) return;

        input.addEventListener("change", e => {

            const file = e.target.files[0];

            if (!file) return;

            const reader = new FileReader();

            reader.onload = event => {

                preview.src = event.target.result;

                showToast(
                    "Profile",
                    "Profile picture updated."
                );

            };

            reader.readAsDataURL(file);

        });

    },

    profileForm() {

        const form = document.getElementById("profileForm");

        if (!form) return;

        form.addEventListener("submit", e => {

            e.preventDefault();

            const name = form.name.value.trim();
            const email = form.email.value.trim();

            if (!name || !email) {

                showToast(
                    "Error",
                    "Please fill all fields."
                );

                return;

            }

            localStorage.setItem("username", name);

            showToast(
                "Success",
                "Profile updated successfully."
            );

        });

    },

    passwordForm() {

        const form = document.getElementById("passwordForm");

        if (!form) return;

        form.addEventListener("submit", e => {

            e.preventDefault();

            const current = form.currentPassword.value.trim();
            const password = form.newPassword.value.trim();
            const confirm = form.confirmPassword.value.trim();

            if (!current || !password || !confirm) {

                showToast(
                    "Error",
                    "Please fill all fields."
                );

                return;

            }

            if (password !== confirm) {

                showToast(
                    "Error",
                    "Passwords do not match."
                );

                return;

            }

            showToast(
                "Success",
                "Password changed successfully."
            );

            form.reset();

        });

    },

    theme() {

        const button = document.getElementById("themeToggle");

        if (!button) return;

        button.addEventListener("click", () => {

            document.body.classList.toggle("dark");

            const dark = document.body.classList.contains("dark");

            localStorage.setItem("theme", dark ? "dark" : "light");

            showToast(
                "Theme",
                dark ? "Dark Mode Enabled" : "Light Mode Enabled"
            );

        });

    },

    logout() {

        const button = document.getElementById("logout");

        if (!button) return;

        button.addEventListener("click", () => {

            localStorage.clear();

            showToast(
                "Logout",
                "Logged out successfully."
            );

            setTimeout(() => {

                window.location.href = "login.html";

            }, 1000);

        });

    }

};

document.addEventListener("DOMContentLoaded", () => {

    Profile.init();

});