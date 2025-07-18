console.warn("Using offline-compatible Leaflet fallback");
// Basic Leaflet compatibility stubs
window.L = {
  map: () => ({ setView: () => {} }),
  tileLayer: () => ({ addTo: () => {} }),
  marker: () => ({ addTo: () => {} })
};