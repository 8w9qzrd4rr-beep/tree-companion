const form = document.getElementById('login-form');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const errorText = document.getElementById('errorText');
const toggleBtn = document.getElementById('toggleVisibility');

// ---------- SHOW / HIDE PASSWORD ----------
toggleBtn.addEventListener('click', () => {
  const isPassword = passwordInput.type === 'password';
  passwordInput.type = isPassword ? 'text' : 'password';
  toggleBtn.innerHTML = isPassword
    ? '<i class="fa fa-eye-slash" aria-hidden="true"></i>'
    : '<i class="fa fa-eye" aria-hidden="true"></i>';
  toggleBtn.setAttribute('aria-label', isPassword ? 'Hide password' : 'Show password');
});

// ---------- BASIC VALIDATION ----------
function isValidEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}

form.addEventListener('submit', (e) => {
  e.preventDefault();
  errorText.textContent = '';

  const email = emailInput.value.trim();
  const password = passwordInput.value;

  if (!email || !isValidEmail(email)) {
    errorText.textContent = 'Enter a valid email address.';
    emailInput.focus();
    return;
  }

  if (!password || password.length < 6) {
    errorText.textContent = 'Password must be at least 6 characters.';
    passwordInput.focus();
    return;
  }

  // Swap this for a real authentication request to your backend/API.
  window.location.href = '/';
});
