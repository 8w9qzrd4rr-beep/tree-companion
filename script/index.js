const reginaBounds = [
  [-104.8000, 50.3500], // Southwest coordinates [lng, lat]
  [-104.4000, 50.5500]  // Northeast coordinates [lng, lat]
];

const map = new maplibregl.Map({
  container: 'map',
  style: 'https://tiles.openfreemap.org/styles/liberty',
  center: [-104.6189, 50.4452],
  zoom: 12,
  minZoom: 1,
  maxZoom: 19,
  maxBounds: reginaBounds
});

map.addControl(new maplibregl.NavigationControl(), 'top-right');

const mapWrap = document.getElementById('map-wrap');
if (window.ResizeObserver) {
  const resizeObserver = new ResizeObserver(() => map.resize());
  resizeObserver.observe(mapWrap);
} else {
  // Fallback for older browsers without ResizeObserver support.
  window.addEventListener('resize', () => map.resize());
  window.addEventListener('orientationchange', () => map.resize());
}

document.addEventListener("DOMContentLoaded", async () => {
  const locationCanvas = document.getElementById("current-location");
  try {
    let loc = await getLocation();
    locationCanvas.textContent = `Lat: ${loc.latitude.toFixed(5)}, Lon: ${loc.longitude.toFixed(5)}`;
    updateMap(loc);
  } catch (err) {
    console.warn(err.message);
    locationCanvas.textContent = "Location unavailable";
  }

  try {
    const response = await fetch('/api/v1/trees');
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const result = await response.json(); 
    // Process the received data here
    alert(JSON.stringify(result));
  } catch (error) {
    console.error("Failed to fetch trees:", error);
  }  
});

function updateMap(loc) {
  const dotElement = document.createElement('div');
  dotElement.style.width = '12px';
  dotElement.style.height = '12px';
  dotElement.style.backgroundColor = '#f63b3b';
  dotElement.style.borderRadius = '50%';
  dotElement.style.border = '2px solid #ffffff';

  new maplibregl.Marker({ element: dotElement })
    .setLngLat([loc.longitude, loc.latitude])
    .addTo(map);
}

function getLocation() {
  return new Promise((resolve, reject) => {
    if (!navigator.geolocation) {
      reject(new Error("Geolocation is not supported by this browser."));
      return;
    }

    navigator.geolocation.getCurrentPosition(
      (position) => {
        resolve({
          latitude: position.coords.latitude,
          longitude: position.coords.longitude,
          accuracy: position.coords.accuracy
        });
      },
      (error) => {
        reject(new Error("Error getting location: " + error.message));
      }
    );
  });
}

// ---------- FAB MENU ----------
const fabBtn = document.getElementById('fabBtn');
const fabOptions = document.getElementById('fab-options');
const fabOverlay = document.getElementById('fab-overlay');

function setFabOpen(open) {
  fabBtn.classList.toggle('open', open);
  fabOptions.classList.toggle('open', open);
  fabOverlay.classList.toggle('open', open);
}

fabBtn.addEventListener('click', () => {
  const isOpen = fabBtn.classList.contains('open');
  setFabOpen(!isOpen);
});

fabOverlay.addEventListener('click', () => setFabOpen(false));

// ---------- ADD TREE FORM ----------
const addTreeOverlay = document.getElementById('add-tree-overlay');
const addTreeSheet = document.getElementById('add-tree-sheet');
const addTreeForm = document.getElementById('add-tree-form');
const cancelAddTree = document.getElementById('cancelAddTree');

function popForm() {
  addTreeOverlay.classList.add('open');
  addTreeSheet.classList.add('open');
  addTreeSheet.setAttribute('aria-hidden', 'false');
}

function closeForm() {
  addTreeOverlay.classList.remove('open');
  addTreeSheet.classList.remove('open');
  addTreeSheet.setAttribute('aria-hidden', 'true');
  addTreeForm.reset();
}

// EL 1 — plantTree opens the form
document.getElementById("plantTree").addEventListener('click', () => {
  setFabOpen(false);
  popForm();

  // ################################################################
  // # TODO: your fetch goes here if the form needs to load anything
  // # (e.g. species list, current location, draft data) before it's
  // # shown to the user.
  // ################################################################
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
  await fetch('/api/v1/add/trees', { method: 'POST', body: formData });
  closeForm();
});