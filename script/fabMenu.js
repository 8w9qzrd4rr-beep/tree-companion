// ---------- FAB MENU ----------
const fabBtn = document.getElementById('fabBtn');
const fabOptions = document.getElementById('fab-options');
const fabOverlay = document.getElementById('fab-overlay');

export function setFabOpen(open) {
  fabBtn.classList.toggle('open', open);
  fabOptions.classList.toggle('open', open);
  fabOverlay.classList.toggle('open', open);
}

fabBtn.addEventListener('click', () => {
  const isOpen = fabBtn.classList.contains('open');
  setFabOpen(!isOpen);
});

fabOverlay.addEventListener('click', () => setFabOpen(false));