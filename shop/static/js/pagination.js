document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".pagination-page");

    const params = new URLSearchParams(window.location.search);
    const currentPage = params.get("page") || "1";

    buttons.forEach(btn => {
        if (btn.textContent.trim() === currentPage) {
            btn.classList.add("active");
        }

        btn.addEventListener("click", () => {
            const page = btn.textContent.trim();
            window.location.search = `?page=${page}`;
        });
    });
});