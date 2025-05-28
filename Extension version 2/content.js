(async () => {
  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  // Получить логин, введённый пользователем
  const { loginSyncUsername } = await chrome.storage.local.get("loginSyncUsername");

  await sleep(5000);  // ⏳ Ждём 5 секунд после открытия страницы

  const loginInput = document.querySelector("input[name='login_name']");
  const passInput = document.querySelector("input[name='login_password']");

  if (loginInput && passInput) {
    loginInput.value = "Cnbr2";
    passInput.value = "maz6ERTYUIOP";

    await sleep(2000);  // Ждём 2 секунды перед нажатием Enter

    passInput.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13 }));
    passInput.form.submit();  // Альтернативный способ запуска формы
  }

  // Ждём полной загрузки и перехода после входа
  await sleep(7000);

  // Удаляем лишние элементы
  document.querySelector(".donate")?.remove();
  await sleep(2000);
  document.querySelector(".rules")?.remove();
  await sleep(2000);
  document.querySelector(".forum")?.remove();
  await sleep(2000);

  // Заменяем приветствие
  document.querySelectorAll(".shortened").forEach(el => {
    el.textContent = loginSyncUsername || "User";
  });
})();

