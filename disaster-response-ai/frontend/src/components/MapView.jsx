import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup, CircleMarker } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const dummyIncidents = [
  { id: 1, lat: -25.75, lng: 28.19, type: "fire", intensity: "high" },
  { id: 2, lat: -26.20, lng: 28.04, type: "fire", intensity: "moderate" },
  { id: 3, lat: -25.8, lng: 28.1, type: "flood", intensity: "low" },
];

const intensityColor = {
  high: "red",
  moderate: "orange",
  low: "blue",
};

export default function MapView() {
  const [incidents, setIncidents] = useState(dummyIncidents);

  return (
    <MapContainer
      center={[-25.75, 28.19]}
      zoom={10}
      style={{ height: "100%", width: "100%" }}
      scrollWheelZoom={false}
    >
      <TileLayer
        attribution='&copy; OpenStreetMap contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {incidents.map(({ id, lat, lng, type, intensity }) => (
        <CircleMarker
          key={id}
          center={[lat, lng]}
          radius={10}
          pathOptions={{ color: intensityColor[intensity] }}
        >
          <Popup>
            <strong>{type.toUpperCase()}</strong> incident<br />
            Intensity: {intensity}
          </Popup>
        </CircleMarker>
      ))}
    </MapContainer>
  );
}
