import { getLocation } from './geolocation.js';
import { updateMapTree } from './mapController.js';
import { setFabOpen } from './fabMenu.js';

// ---------- ADD TREE FORM ----------
const addTreeOverlay = document.getElementById('add-tree-overlay');
const addTreeSheet = document.getElementById('add-tree-sheet');
const addTreeForm = document.getElementById('add-tree-form');
const cancelAddTree = document.getElementById('cancelAddTree');

export function popForm() {
  addTreeOverlay.classList.add('open');
  addTreeSheet.classList.add('open');
  addTreeSheet.setAttribute('aria-hidden', 'false');
}

export function closeForm() {
  addTreeOverlay.classList.remove('open');
  addTreeSheet.classList.remove('open');
  addTreeSheet.setAttribute('aria-hidden', 'true');
  addTreeForm.reset();
}

// EL 1 — plantTree opens the form
document.getElementById("plantTree").addEventListener('click', () => {
  setFabOpen(false);
  popForm();
  
});

// EL 2 — cancel closes the form, no save
cancelAddTree.addEventListener('click', () => {
  closeForm();
});

// clicking the dark backdrop behaves the same as cancel
addTreeOverlay.addEventListener('click', () => {
  closeForm();
});

// EL 3 — submit closes the form after saving
addTreeForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const formData = new FormData(addTreeForm);
  const location = await getLocation();
  formData.append('loc', JSON.stringify(location));
  await fetch('/api/v1/add/trees', { method: 'POST', body: formData});
  updateMapTree(location);
  closeForm();
});