const trigger = document.querySelector('#menu-trigger');
const menu = document.querySelector('#mobile-menu');
trigger.addEventListener('click', () => { menu.hidden = !menu.hidden; });
document.querySelector('#contact').addEventListener('submit', event => {
  event.preventDefault();
  document.querySelector('#error').textContent = 'شماره واردشده معتبر نیست';
});
