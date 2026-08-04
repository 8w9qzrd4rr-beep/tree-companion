import { getLocation } from './geolocation.js';
import { updateMap, updateMapTree } from './mapController.js';
import { fetchTrees } from './api.js';
import './fabMenu.js';
import './addTreeForm.js';

document.addEventListener("DOMContentLoaded", async () => {
  const locationCanvas = document.getElementById("current-location");
  let currentLoc;

  // 1. Fetch location explicitly
  try {
    currentLoc = await getLocation();
    locationCanvas.textContent = `Lat: ${currentLoc.latitude.toFixed(5)}, Lon: ${currentLoc.longitude.toFixed(5)}`;
  } catch (err) {
    console.warn("Location error:", err.message);
    locationCanvas.textContent = "Location unavailable";
    return;
  }

  // 2. Initialize the user's location on the map
  try {
    updateMapTree(currentLoc);
  } catch (err) {
    console.error("Map initialization failed:", err);
  }

  // 3. Fetch and plot trees
  try {
    const result = await fetchTrees();
    const treeList = result.data;
    treeList.forEach(function (item) {
      const loc = {
        latitude: item.latitude,
        longitude: item.longitude
      };
      updateMap(loc, map);
    });
  } catch (error) {
    console.error("Failed to load trees:", error);
  }
});