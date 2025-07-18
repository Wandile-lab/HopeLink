import React, { useState, useEffect } from 'react';
import ChatBot from './components/ChatBot';
import DisasterMap from './components/DisasterMap';
import Dashboard from './components/Dashboard';
import NearbyShelters from './components/NearbyShelters';


const sampleIncidents = [
  { lat: 51.51, lng: -0.1, type: 'Flood', description: 'River overflowed near Main St.' },
  { lat: 51.507, lng: -0.08, type: 'Fire', description: 'Wildfire reported in nearby forest.' }
];

const mockStats = [
  { label: 'Active Emergencies', value: 5 },
  { label: 'Shelters Open', value: 12 },
  { label: 'Responders Deployed', value: 78 }
];

export default function App() {
  const [loading, setLoading] = useState(true);
  const [isOffline, setIsOffline] = useState(!navigator.onLine);

  useEffect(() => {
    const timer = setTimeout(() => setLoading(false), 10000); // 10 seconds loading
    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    const handleOnline = () => setIsOffline(false);
    const handleOffline = () => setIsOffline(true);
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  if (loading) {
    return (
      <div style={{
        position: 'fixed',
        inset: 0,
        background: 'linear-gradient(135deg, #0d1b2a 0%, #1b263b 100%)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        color: '#f97316',
        fontSize: '1.5rem',
        fontWeight: 'bold',
        flexDirection: 'column',
        textAlign: 'center',
        padding: '20px',
        zIndex: 9999,
      }}>
        <div className="loading-spinner" style={{
          marginBottom: '20px',
          border: '8px solid #f3f3f3',
          borderTop: '8px solid #f97316',
          borderRadius: '50%',
          width: '60px',
          height: '60px',
          animation: 'spin 1.5s linear infinite'
        }} />
        Loading HopeLink...
        <div style={{ marginTop: '10px', fontSize: '1rem', color: '#ffb347' }}>
          Note: Currently using mock samples, real location tracking coming soon!
        </div>
        <style>{`
          @keyframes spin {
            0% { transform: rotate(0deg);}
            100% { transform: rotate(360deg);}
          }
        `}</style>
      </div>
    );
  }

  return (
    <div style={{
      padding: '20px',
      background: 'linear-gradient(to bottom right, #0d1a2d, #122a38)',
      color: 'white',
      minHeight: '100vh',
      overflowY: 'auto',
      display: 'flex',
      flexDirection: 'column',
    }}>
      {isOffline && (
        <div style={{
          backgroundColor: '#b91c1c',
          color: 'white',
          padding: '12px',
          textAlign: 'center',
          fontWeight: 'bold',
          borderBottom: '3px solid #7f1d1d',
          zIndex: 10000
        }}>
          ⚠️ You are offline. Some features may not work properly.
        </div>
      )}

      <h1 style={{ textAlign: 'center', marginBottom: '20px' }}>
        🚨 HopeLink - AI Disaster Assistant
      </h1>

      {/* Location tracking banner */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '8px',
        color: '#f97316',
        fontWeight: '600',
        marginBottom: 12,
        fontSize: '0.95rem',
        userSelect: 'none',
      }}>
        <span className="blinking-dot" aria-label="Location tracking active" role="img">◉</span>
        <span>Your location is being tracked for emergency assistance.</span>
      </div>

      <h2 style={{ 
        textAlign: 'center', 
        marginBottom: 24, 
        fontWeight: 'bold', 
        color: '#f97316',
        letterSpacing: '0.05em'
      }}>
        Disaster Stats
      </h2>

      <div style={{
        display: 'flex',
        justifyContent: 'center',
        flexWrap: 'wrap',
        gap: '20px',
        marginBottom: 40,
      }}>
        {mockStats.map((stat, i) => (
          <div key={i} style={{
            backgroundColor: '#1e3a8a',
            padding: '18px 24px',
            borderRadius: '14px',
            minWidth: '140px',
            textAlign: 'center',
            boxShadow: '0 0 10px rgba(249, 115, 22, 0.6)'
          }}>
            <strong style={{ fontSize: '1.1rem' }}>{stat.label}</strong><br />
            <span style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>{stat.value}</span>
          </div>
        ))}
      </div>

      <h2 style={{ 
        textAlign: 'center', 
        marginBottom: 16, 
        fontWeight: 'bold', 
        color: '#f97316',
        letterSpacing: '0.05em'
      }}>
        Emergency Resources
      </h2>

      <div style={{
        display: 'flex',
        justifyContent: 'center',
        flexWrap: 'wrap',
        gap: '16px',
        marginBottom: 32,
      }}>
        <div style={{
          backgroundColor: '#1e40af',
          padding: '14px 20px',
          borderRadius: '12px',
          minWidth: '180px',
          color: 'white',
          boxShadow: '0 0 8px rgba(255, 165, 0, 0.5)',
        }}>
          <strong>Shelter Hotline</strong><br />
          0800 001 005
        </div>

        <div style={{
          backgroundColor: '#1e40af',
          padding: '14px 20px',
          borderRadius: '12px',
          minWidth: '180px',
          color: 'white',
          boxShadow: '0 0 8px rgba(255, 165, 0, 0.5)',
        }}>
          <strong>Medical Emergency</strong><br />
          10177
        </div>

        <div style={{
          backgroundColor: '#1e40af',
          padding: '14px 20px',
          borderRadius: '12px',
          minWidth: '180px',
          color: 'white',
          boxShadow: '0 0 8px rgba(255, 165, 0, 0.5)',
        }}>
          <strong>Report Fire</strong><br />
          112
        </div>
      </div>

      <div className="app-container" style={{
        display: 'flex',
        gap: '24px',
        justifyContent: 'center',
        flexWrap: 'nowrap',
        flexGrow: 1,
      }}>
        <div style={{ flex: '1 1 350px', maxWidth: 450, display: 'flex', flexDirection: 'column' }}>
          <ChatBot />
        </div>

        <div style={{ flex: '1 1 600px', maxWidth: 600 }}>
          <DisasterMap incidents={sampleIncidents} />
          <NearbyShelters />
        </div>

        <div style={{ flex: '1 1 350px', maxWidth: 400 }}>
          <Dashboard />
        </div>
      </div>
    </div>
  );
}
