// Derive avatar initials from the display name.
const nameEl = document.getElementById('profileName');
const avatarEl = document.getElementById('avatarInitials');

function setInitials(name) {
  const initials = name
    .split(' ')
    .filter(Boolean)
    .slice(0, 2)
    .map(w => w[0].toUpperCase())
    .join('');
  avatarEl.textContent = initials || '?';
}

setInitials(nameEl.textContent.trim());

// Log out -> send back to the login screen.
document.getElementById('logoutBtn').addEventListener('click', () => {
  const confirmed = window.confirm('Log out of TreeSaathi?');
  if (confirmed) {
    window.location.href = '/login';
  }
});
