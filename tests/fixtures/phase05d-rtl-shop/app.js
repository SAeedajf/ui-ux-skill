const trigger = document.querySelector('#menu-trigger');
const menu = document.querySelector('#mobile-menu');
const form = document.querySelector('#contact');
const phone = document.querySelector('#phone');
const error = document.querySelector('#error');
const status = document.querySelector('#status');

function setMenuOpen(open) {
  menu.hidden = !open;
  trigger.setAttribute('aria-expanded', String(open));
  trigger.setAttribute('aria-label', open ? 'بستن منو' : 'باز کردن منو');
}

trigger.addEventListener('click', () => setMenuOpen(menu.hidden));
menu.addEventListener('keydown', event => {
  if (event.key === 'Escape') {
    setMenuOpen(false);
    trigger.focus();
  }
});

function showError(message) {
  error.textContent = message;
  phone.setAttribute('aria-invalid', 'true');
  status.textContent = '';
  document.querySelector('#phone').focus();
}

form.addEventListener('submit', event => {
  event.preventDefault();
  const value = phone.value.trim();

  if (!value) {
    showError('شماره تماس را وارد کنید.');
    return;
  }
  if (!/^09[0-9]{9}$/.test(value)) {
    showError('شماره باید با ۰۹ شروع شود و ۹ رقم انگلیسی دیگر داشته باشد.');
    return;
  }

  error.textContent = '';
  phone.setAttribute('aria-invalid', 'false');
  status.textContent = 'شماره در این آزمون معتبر است؛ اطلاعات ارسال نشد.';
});
