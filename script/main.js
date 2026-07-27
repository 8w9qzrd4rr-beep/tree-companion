import { getLocation } from './geolocation.js';
import { updateMap, updateMapTree } from './mapController.js';
import { fetchTrees } from './api.js';
import './fabMenu.js';
import './addTreeForm.js';

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
    const result = await fetchTrees();
    // Process the received data here
    const treeList = result.data;
    treeList.forEach(function (item) {
    const loc = {
    latitude: item.latitude,
    longitude: item.longitude
  };
  updateMapTree(loc);
});
    alert(JSON.stringify(result));
  } catch (error) {
    console.error("Failed to fetch trees:", error);
  }
});