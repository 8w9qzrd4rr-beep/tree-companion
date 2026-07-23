document.addEventListener("DOMContentLoaded", async () => {
    const locationCanvas = document.getElementById("current-location")
    try {
        let loc = await getLocation();
        locationCanvas.textContent = `Lat: ${loc.latitude}, Lon: ${loc.longitude}`;
        updateMap(loc);

    } catch (err) {
        alert(err.message);
    }
});

function updateMap(loc){
    const dotElement = document.createElement('div');
    dotElement.style.width = '12px';
    dotElement.style.height = '12px';
    dotElement.style.backgroundColor = '#f63b3b'; // Blue color
    dotElement.style.borderRadius = '50%';        // Makes it a circle
    dotElement.style.border = '2px solid #ffffff';

    const marker = new maplibregl.Marker({ element: dotElement })
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
    const reginaBounds = [
      [-104.8000, 50.3500], // Southwest coordinates [lng, lat]
      [-104.4000, 50.5500]  // Northeast coordinates [lng, lat]
    ];

    const map = new maplibregl.Map({
      container: 'map',
      style: 'https://tiles.openfreemap.org/styles/liberty',
      center: [-104.6189, 50.4452],
      zoom: 4,
      minZoom: 1,
      maxZoom: 19,
      maxBounds: reginaBounds
    });

    map.addControl(new maplibregl.NavigationControl(), 'top-right');

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