const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnlogin-popup');
const iconclose = document.querySelector('.icon-close');

loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');       
});

registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
});

iconclose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');       
});