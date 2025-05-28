const login2 = "Cnbr2";
const password2 = "maz6ERTYUIOP";

(async () => {
    const delay = ms => new Promise(res => setTimeout(res, ms));

    const loginInput = document.querySelector('input[name="login_name"]');
    const passwordInput = document.querySelector('input[name="login_password"]');

    if (!loginInput || !passwordInput) return;

    loginInput.value = login2;
    passwordInput.value = password2;

    await delay(500);

    const form = loginInput.closest("form");
    if (form) {
        form.submit();
    } else {
        passwordInput.dispatchEvent(new KeyboardEvent("keydown", {
            key: "Enter", code: "Enter", keyCode: 13, which: 13, bubbles: true
        }));
    }
})();
