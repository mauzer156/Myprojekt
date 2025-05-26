document.getElementById("login-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const status = document.getElementById("status");

  status.textContent = "⏳ Проверка...";
  
  try {
    const response = await fetch("http://127.0.0.1:8000/api/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (data.success) {
      status.textContent = "✅ Успешный вход!";
      // здесь можно сделать переход или сообщение скрипту
    } else {
      status.textContent = "❌ Ошибка: Неверные данные";
    }
  } catch (error) {
    status.textContent = "🚫 Сервер недоступен";
  }
});

