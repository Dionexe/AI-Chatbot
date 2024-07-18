const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');
const sidebarToggle = document.getElementById('sidebar-toggle');
const sidebar = document.querySelector('.sidebar');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
    sidebar.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
    sidebar.classList.remove("active");
});

sidebarToggle.addEventListener('click', () => {
    sidebar.classList.toggle('sidebar-open');
});