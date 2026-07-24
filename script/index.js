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

// ---------- KEEP THE MAP CANVAS IN SYNC WITH ITS CONTAINER ----------
// The app shell's size changes between phone / tablet / desktop
// breakpoints (see css/index.css), and mobile browsers resize their
// viewport when the address bar shows/hides. MapLibre caches the
// canvas size, so it needs an explicit resize() call whenever the
// #map container itself changes size.
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

document.querySelectorAll('.fab-option').forEach(opt => {
  opt.addEventListener('click', () => {
    // handle each action here
    console.log('Selected action:', opt.dataset.action);
    setFabOpen(false);
  });
});

document.getElementById("plantTree").addEventListener('click', () => {
  alert("Hello");
});