document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("sideBarToogle");
    const sidebar = document.getElementById("sidebar");

    if (toggleBtn && sidebar) {
        toggleBtn.addEventListener("click", function () {
            sidebar.classList.toggle("collapse");
        });
    }
});
