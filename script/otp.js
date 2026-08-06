const emailTarget = document.getElementById('emailTarget');
  const boxesWrap = document.getElementById('otpBoxes');
  const boxes = Array.from(boxesWrap.querySelectorAll('input'));
  const form = document.getElementById('otp-form');
  const errorText = document.getElementById('errorText');
  const verifyBtn = document.getElementById('verifyBtn');
  const resendLabel = document.getElementById('resendLabel');
  const resendTimer = document.getElementById('resendTimer');
  const resendBtn = document.getElementById('resendBtn');

  const storedEmail = sessionStorage.getItem('signup_email');
  if (storedEmail) emailTarget.textContent = storedEmail;

  function updateVerifyState() {
    const code = boxes.map(b => b.value).join('');
    verifyBtn.disabled = code.length !== 6;
  }

  boxes.forEach((box, i) => {
    box.addEventListener('input', () => {
      box.value = box.value.replace(/[^0-9]/g, '').slice(0, 1);
      box.classList.toggle('filled', box.value.length === 1);
      if (box.value && i < boxes.length - 1) boxes[i + 1].focus();
      errorText.textContent = '';
      updateVerifyState();
    });

    box.addEventListener('keydown', (e) => {
      if (e.key === 'Backspace' && !box.value && i > 0) {
        boxes[i - 1].focus();
      }
    });

    box.addEventListener('paste', (e) => {
      e.preventDefault();
      const pasted = (e.clipboardData.getData('text') || '').replace(/[^0-9]/g, '').slice(0, 6);
      pasted.split('').forEach((ch, idx) => {
        if (boxes[idx]) {
          boxes[idx].value = ch;
          boxes[idx].classList.add('filled');
        }
      });
      const next = boxes[Math.min(pasted.length, boxes.length - 1)];
      if (next) next.focus();
      updateVerifyState();
    });
  });

  boxes[0].focus();

  // Resend countdown
  let seconds = 30;
  const countdown = setInterval(() => {
    seconds -= 1;
    if (seconds <= 0) {
      clearInterval(countdown);
      resendLabel.style.display = 'none';
      resendBtn.style.display = 'inline';
    } else {
      resendTimer.textContent = `${seconds}s`;
    }
  }, 1000);

  resendBtn.addEventListener('click', async () => {
    resendBtn.disabled = true;
    try {
        await fetch('/api/auth/resend-otp', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: storedEmail })
      });
      resendBtn.style.display = 'none';
      resendLabel.style.display = 'inline';
      seconds = 30;
      resendTimer.textContent = `${seconds}s`;
      const restarted = setInterval(() => {
        seconds -= 1;
        if (seconds <= 0) {
          clearInterval(restarted);
          resendLabel.style.display = 'none';
          resendBtn.style.display = 'inline';
          resendBtn.disabled = false;
        } else {
          resendTimer.textContent = `${seconds}s`;
        }
      }, 1000);
    } catch {
      resendBtn.disabled = false;
      errorText.textContent = 'Could not resend code. Try again.';
    }
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    errorText.textContent = '';

    const code = boxes.map(b => b.value).join('');
    if (code.length !== 6) {
      errorText.textContent = 'Enter all 6 digits.';
      return;
    }
    const formData = new URLSearchParams();
    formData.append('email', storedEmail);
    formData.append('code', code);
    try {
      const res = await fetch('/api/auth/verify-otp', {
        method: 'POST',
        body: formData
      });
      const isValid = await res.json();

      if (res.ok && isValid === true) {
        alert("Verified!! Login Now");
        window.location.href = '/signup/info';
        } else {
            alert("Nope Sir");
        }

    } catch (err) {
      errorText.textContent = err.message || 'Invalid code. Please try again.';
      boxes.forEach(b => { b.value = ''; b.classList.remove('filled'); });
      boxes[0].focus();
      updateVerifyState();
    }
  });