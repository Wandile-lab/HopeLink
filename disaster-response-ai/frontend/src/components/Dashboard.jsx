// src/components/Dashboard.jsx
import React, { useEffect, useState } from 'react';

const mockAidData = [
  { type: 'Water', status: 'Available', quantity: '500L' },
  { type: 'Food Packs', status: 'Low', quantity: '120 units' },
  { type: 'Medical Kits', status: 'Available', quantity: '75 kits' },
];

const notifications = [
  'New shelter opened in District 4.',
  'Medical team dispatched to Zone B.',
  'Supply truck delayed due to weather.',
  'Volunteers needed in Zone C.',
  'Flood alert: Evacuate low-lying areas!',
];

const mockAidRequests = [
  { name: 'John D.', type: 'Medical', time: '10:32 AM' },
  { name: 'Amina K.', type: 'Evacuation', time: '10:35 AM' },
  { name: 'Carlos R.', type: 'Food', time: '10:42 AM' },
];

const shelters = [
  { name: 'Shelter A', status: 'Open' },
  { name: 'Shelter B', status: 'Full' },
  { name: 'Shelter C', status: 'Limited Space' },
];

const statusColors = {
  Open: '#10b981',
  Full: '#ef4444',
  'Limited Space': '#f59e0b',
};

const Dashboard = () => {
  const [currentNotification, setCurrentNotification] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentNotification((prev) => (prev + 1) % notifications.length);
    }, 4000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{
      minWidth: '280px',
      padding: '20px',
      backgroundColor: '#0f172a',
      borderLeft: '2px solid #2563eb',
      color: '#e0e7ff',
      height: '100%',
      overflowY: 'auto'
    }}>
      <h2 style={{
        fontWeight: 'bold',
        color: '#f97316',
        marginBottom: '16px',
        textAlign: 'center'
      }}>
        Aid Distribution Dashboard
      </h2>

      {/* 🔁 Notification Panel */}
      <div style={{
        background: '#1f2937',
        padding: '10px 16px',
        borderRadius: '8px',
        marginBottom: '20px',
        borderLeft: '4px solid #f97316',
        fontStyle: 'italic',
        animation: 'fadeIn 1s ease-in'
      }}>
        🔔 {notifications[currentNotification]}
      </div>

      {/* 🧾 Aid Request Submission Log */}
      <div style={{ marginBottom: '20px' }}>
        <h3 style={{ fontSize: '1.1rem', marginBottom: '8px' }}>Recent Aid Requests</h3>
        {mockAidRequests.map((req, idx) => (
          <div key={idx} style={{
            background: '#334155',
            padding: '8px 12px',
            borderRadius: '8px',
            marginBottom: '6px'
          }}>
            <strong>{req.name}</strong> requested <em>{req.type}</em> at {req.time}
          </div>
        ))}
      </div>

      {/* 🧺 Distribution Data (original) */}
      {mockAidData.map((item, idx) => (
        <div key={idx} style={{
          background: '#1e3a8a',
          padding: '14px 18px',
          borderRadius: '10px',
          marginBottom: '14px',
          textAlign: 'center'
        }}>
          <h4 style={{ marginBottom: '6px', fontSize: '1rem' }}>{item.type}</h4>
          <p>Status: <strong>{item.status}</strong></p>
          <p>Quantity: <strong>{item.quantity}</strong></p>
        </div>
      ))}

    </div>
  );
};

export default Dashboard;
