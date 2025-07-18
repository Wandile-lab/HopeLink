import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const redIcon = new L.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
   iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],   // doubled shadow size to match
});

const DisasterMap = ({ incidents }) => {
  // South Africa coordinates as fallback default
  const defaultPosition = [-29.0, 24.0];

  const [position, setPosition] = useState(defaultPosition);

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(
      (pos) => setPosition([pos.coords.latitude, pos.coords.longitude]),
      () => setPosition(defaultPosition) // fallback to SA
    );
  }, []);

  return (
    <MapContainer center={position} zoom={6} style={{ height: '400px', borderRadius: '16px' }} aria-label="Disaster Map">
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; OpenStreetMap contributors'
      />
      {incidents.map((incident, idx) => (
        <Marker key={idx} position={[incident.lat, incident.lng]} icon={redIcon}>
          <Popup>
            <strong>{incident.type}</strong><br />
            {incident.description}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default DisasterMap;
