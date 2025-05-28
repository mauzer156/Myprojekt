(async () => {
    const delay = ms => new Promise(res => setTimeout(res, ms));

    await delay(2000); // Ждём загрузки

    document.querySelector(".donate")?.remove();
    document.querySelector(".rules")?.remove();
    document.querySelector(".forum")?.remove();

    await delay(2000); // Ждём перед изменением ника

    document.querySelectorAll(".shortened").forEach(el => {
        el.textContent = "Cnbr2";
    });
})();
