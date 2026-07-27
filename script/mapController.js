const reginaBounds = [
  [-104.8000, 50.3500], // Southwest coordinates [lng, lat]
  [-104.4000, 50.5500]  // Northeast coordinates [lng, lat]
];

export const map = new maplibregl.Map({
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

export function updateMap(loc) {
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

export function updateMapTree(loc) {
  let marker = new maplibregl.Marker()
    .setLngLat([loc.longitude, loc.latitude])
    .addTo(map);
}