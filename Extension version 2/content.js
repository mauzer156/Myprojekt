(async () => {
  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  // Получить логин, введённый пользователем (сохранённый в расширении)
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

  // --- Добавляем отслеживание кликов по кнопкам и отправку логов ---

  async function sendLog(action) {
    try {
      const response = await fetch("https://myprojekt.onrender.com/api/track_click/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          login: loginSyncUsername || "Unknown",
          action: action
        })
      });
      if (response.ok) {
        console.log(`Лог отправлен: ${action}`);
      } else {
        console.error("Ошибка при отправке лога:", response.statusText);
      }
    } catch (err) {
      console.error("Ошибка сети при отправке лога:", err);
    }
  }

  function handleClick(event) {
    const target = event.target;

    // Если клик по кнопке "Личный кабинет"
    if (target.classList.contains("user_panel_navigation_cp")) {
      sendLog("Личный кабинет");
    }
    // Если клик по кнопке "Пополнить"
    else if (target.classList.contains("user_panel_balance_add")) {
      sendLog("Пополнить");
    }
  }

  // Слушаем клики по всему документу (делегирование)
  document.addEventListener("click", handleClick);

})();
