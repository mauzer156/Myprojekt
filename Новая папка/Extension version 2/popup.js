document.getElementById("login-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const status = document.getElementById("status");

  status.textContent = "⏳ Проверка...";

  try {
    const response = await fetch("https://myprojekt.onrender.com/api/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    // response.json() должен вернуть true или false
    const isSuccess = await response.json();

    if (isSuccess === true) {
      status.textContent = "✅ Успешный вход!";
    } else {
      status.textContent = "❌ Ошибка: Неверные данные";
    }
  } catch (error) {
    status.textContent = "🚫 Сервер недоступен";
  }
});


