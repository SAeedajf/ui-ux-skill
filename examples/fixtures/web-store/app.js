const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.site-nav');
menuButton.addEventListener('click', () => {
  const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!isOpen));
  menuButton.setAttribute('aria-label', isOpen ? 'باز کردن منوی ناوبری' : 'بستن منوی ناوبری');
  navigation.classList.toggle('open', !isOpen);
});
navigation.addEventListener('click', (event) => {
  if (event.target.closest('a') && window.matchMedia('(max-width: 760px)').matches) {
    navigation.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'باز کردن منوی ناوبری');
  }
});
document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape' || !navigation.classList.contains('open')) return;
  navigation.classList.remove('open');
  menuButton.setAttribute('aria-expanded', 'false');
  menuButton.setAttribute('aria-label', 'باز کردن منوی ناوبری');
  menuButton.focus();
});
let cartCount = 0;
document.querySelectorAll('.add-button').forEach((button) => button.addEventListener('click', () => {
  cartCount += 1;
  document.querySelector('#cart-count').textContent = new Intl.NumberFormat('fa-IR').format(cartCount);
}));
const form = document.querySelector('#newsletter-form');
const email = document.querySelector('#email');
const message = document.querySelector('#form-message');
const submit = document.querySelector('#submit-button');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  message.hidden = false;
  if (!email.value || !email.validity.valid) {
    email.setAttribute('aria-invalid', 'true');
    email.setAttribute('aria-describedby', 'email-hint form-message');
    message.textContent = 'لطفاً یک نشانی ایمیل معتبر وارد کن.';
    email.focus();
    return;
  }
  email.setAttribute('aria-invalid', 'false');
  email.setAttribute('aria-describedby', 'email-hint');
  submit.disabled = true;
  submit.textContent = 'در حال ثبت…';
  message.textContent = '';
  window.setTimeout(() => {
    submit.disabled = false;
    submit.textContent = 'عضویت';
    message.textContent = email.value.endsWith('.fail')
      ? 'ارتباط برقرار نشد. دوباره تلاش کن؛ ایمیلت پاک نشده است.'
      : 'عضویتت ثبت شد. ممنون!';
  }, 500);
});
