  import{signUpRequest} from './api.js'

  const form = document.getElementById('signup-form');
  const usernameInput = document.getElementById('username');
  const emailInput = document.getElementById('email');
  const passwordInput = document.getElementById('password');
  const toggleBtn = document.getElementById('toggleVisibility');
  const strengthMeter = document.getElementById('strengthMeter');
  const usernameHint = document.getElementById('usernameHint');
  const errorText = document.getElementById('errorText');

  // Show / hide password
  toggleBtn.addEventListener('click', () => {
    const isHidden = passwordInput.type === 'password';
    passwordInput.type = isHidden ? 'text' : 'password';
    toggleBtn.innerHTML = isHidden
      ? '<i class="fa fa-eye-slash" aria-hidden="true"></i>'
      : '<i class="fa fa-eye" aria-hidden="true"></i>';
  });

  // Password strength meter
  passwordInput.addEventListener('input', () => {
    const val = passwordInput.value;
    let score = 0;
    if (val.length >= 8) score++;
    if (/[A-Z]/.test(val)) score++;
    if (/[0-9]/.test(val)) score++;
    if (/[^A-Za-z0-9]/.test(val)) score++;

    strengthMeter.className = 'strength-meter';
    if (val.length === 0) return;
    if (score <= 1) strengthMeter.classList.add('weak');
    else if (score === 2) strengthMeter.classList.add('fair');
    else if (score === 3) strengthMeter.classList.add('good');
    else strengthMeter.classList.add('strong');
  });

  // Username availability check (placeholder — wire up to your API)
  let usernameTimer;
  usernameInput.addEventListener('input', () => {
    clearTimeout(usernameTimer);
    const val = usernameInput.value.trim();
    usernameHint.textContent = '';
    usernameHint.className = 'hint-text';

    if (val.length < 3) return;

    usernameTimer = setTimeout(async () => {
      try {
        // Replace with a real availability check, e.g.:
        // const res = await fetch(`/api/users/check-username?u=${encodeURIComponent(val)}`);
        // const { available } = await res.json();
        const available = true;
        usernameHint.textContent = available ? 'Username is available' : 'Username is already taken';
        usernameHint.classList.add(available ? 'available' : 'taken');
      } catch {
        // Fail silently — server will re-validate on submit
      }
    }, 400);
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    errorText.textContent = '';

    const username = usernameInput.value.trim();
    const email = emailInput.value.trim();
    const password = passwordInput.value;

    if (username.length < 3) {
      errorText.textContent = 'Username must be at least 3 characters.';
      return;
    }
    if (!/^\S+@\S+\.\S+$/.test(email)) {
      errorText.textContent = 'Enter a valid email address.';
      return;
    }
    if (password.length < 8) {
      errorText.textContent = 'Password must be at least 8 characters.';
      return;
    }
    
    try {
      signUpRequest(username,email,password);
      sessionStorage.setItem('signup_email', email);
      window.location.href = "/signup/verify";
    } catch (err) {
      errorText.textContent = err.message || 'Something went wrong. Please try again.';
    }
  });