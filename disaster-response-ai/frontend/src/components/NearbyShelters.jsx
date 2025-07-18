import React from 'react';

const shelters = [
  { name: 'Shelter A', status: 'Open' },
  { name: 'Shelter B', status: 'Full' },
  { name: 'Shelter C', status: 'Limited Space' },
];

const statusColors = {
  Open: '#10b981',        // green
  Full: '#ef4444',        // red
  'Limited Space': '#f59e0b',  // orange
};

const NearbyShelters = () => {
  return (
    <div style={{
      backgroundColor: '#0f172a',
      padding: '20px',
      borderTop: '2px solid #2563eb',
      borderRadius: '0 0 12px 12px',
      color: '#e0e7ff',
      marginTop: '16px',
      maxWidth: 600,
      marginLeft: 'auto',
      marginRight: 'auto',
    }}>
      <h3 style={{ fontSize: '1.3rem', marginBottom: '16px', color: '#f97316', textAlign: 'center' }}>
         Nearby Shelters
      </h3>
      {shelters.map((shelter, idx) => (
        <div key={idx} style={{
          background: '#1e293b',
          padding: '10px 12px',
          borderRadius: '8px',
          marginBottom: '8px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center'
        }}>
          <span>{shelter.name}</span>
          <span style={{
            backgroundColor: statusColors[shelter.status],
            color: '#fff',
            padding: '2px 10px',
            borderRadius: '6px',
            fontSize: '0.85rem'
          }}>
            {shelter.status}
          </span>
        </div>
      ))}
    </div>
  );
};

export default NearbyShelters;
