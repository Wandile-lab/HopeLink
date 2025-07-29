import React, { useState, useEffect, useRef } from 'react';
import '../styles/chatbot.css';

const quickReplies = [
  'Where’s the nearest shelter?',
  'Report emergency',
  'How can I get medical help?',
  'Are roads open?',
];

const commonResponses = {
  'report emergency': 'Please provide details of the emergency, and our team will respond ASAP.',
  'where’s the nearest shelter?': 'The nearest shelter is 2 km away at Central Community Hall.',
  'are roads open?': 'Some roads are closed due to flooding, please check the map for updates.',
  'how can i get medical help?': 'Medical help is available at City Hospital and Mobile Clinics near you.',
};

export default function ChatBot() {
  const [messages, setMessages] = useState([
    { role: 'bot', text: 'Hello, I’m HopeLink. How can I assist you today?' },
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [showDangerModal, setShowDangerModal] = useState(false);

  const messagesRef = useRef(null);

  useEffect(() => {
    if (messagesRef.current) {
      messagesRef.current.scrollTop = messagesRef.current.scrollHeight;
    }
  }, [messages]);

  // Modified sendMessage to call AI backend if no quick common response found
  const sendMessage = async (messageText) => {
  const userMessage = messageText || input.trim();
  if (!userMessage) return;

  setMessages((msgs) => [...msgs, { role: 'user', text: userMessage }]);
  setInput('');
  setIsTyping(true);

  const lower = userMessage.toLowerCase();
  const responseEntry = Object.entries(commonResponses).find(([key]) =>
    lower.includes(key)
  );

  if (responseEntry) {
    setTimeout(() => {
      setMessages((msgs) => [
        ...msgs,
        { role: 'bot', text: responseEntry[1] },
      ]);
      setIsTyping(false);
    }, 1200);
  } else {
    try {
      const res = await fetch('http://127.0.0.1:8000/prediction/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage }),
      });

      if (!res.ok) {
        throw new Error(`Server error: ${res.statusText}`);
      }

      const data = await res.json();

    const aiResponseText = data.response_message || `Detected disaster: ${data.disaster_type} (Confidence: ${Math.round(data.confidence * 100)}%)\nUrgency: ${data.urgency}`;

      setMessages((msgs) => [
        ...msgs,
        {
          role: 'bot',
          text: aiResponseText,
          urgency: data.urgency,
        },
      ]);
    } catch (error) {
      setMessages((msgs) => [
        ...msgs,
        {
          role: 'bot',
          text: "Sorry, I'm having trouble contacting the AI service right now.",
        },
      ]);
    } finally {
      setIsTyping(false);
    }
  }
};


  const handleQuickReply = (text) => {
    sendMessage(text);
  };

  // New function for Report Danger button click
  const handleReportDanger = () => {
    setShowDangerModal(false);
    const dangerMsg = '🚨 Reporting danger... Help is on the way soon. Please make sure your location is on.';
    setMessages((msgs) => [...msgs, { role: 'user', text: dangerMsg }]);
    setIsTyping(true);
    setTimeout(() => {
      setMessages((msgs) => [
        ...msgs,
        { role: 'bot', text: 'Thank you for reporting. We are tracking your location and dispatching assistance.' },
      ]);
      setIsTyping(false);
    }, 1200);
  };

  return (
    <div className="chat-container">
      <h2 className="chat-title">HopeLink Assistant</h2>

      <div className="chat-messages" ref={messagesRef} style={{ maxHeight: '400px', overflowY: 'auto' }}>
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`chat-message ${msg.role}`}
            style={{
              backgroundColor:
                msg.role === 'bot' && msg.urgency === 'high'
                  ? '#b91c1c'
                  : undefined,
              boxShadow:
                msg.role === 'bot' && msg.urgency === 'high'
                  ? '0 0 10px 3px rgba(185, 28, 28, 0.8)'
                  : undefined,
            }}
          >
            <div className="chat-bubble">
              <strong>{msg.role === 'bot' ? 'HopeLink Bot' : 'You'}</strong>: {msg.text}
            </div>
          </div>
        ))}
        {isTyping && (
          <div className="chat-message bot typing">
            <div className="chat-bubble typing-indicator">
              <span></span><span></span><span></span>
            </div>
          </div>
        )}
      </div>

      {/* New location tracking message */}
      <div className="tracking-indicator">
        <span className="dot">◉</span>
        Your location is being tracked
      </div>

      <div className="quick-replies">
        {quickReplies.map((reply, idx) => (
          <button
            key={idx}
            className="quick-reply-button"
            onClick={() => handleQuickReply(reply)}
          >
            {reply}
          </button>
        ))}
      </div>

      <div className="chat-input-area">
        <input
          className="chat-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Type your message..."
        />
        <button className="send-button" onClick={() => sendMessage()}>
          Send
        </button>
        <button className="danger-button" onClick={handleReportDanger}>
          {' '}
          Report Danger
        </button>
      </div>

      {showDangerModal && (
        <div className="danger-modal">
          <div className="danger-modal-content">
            <h3>🚨 Report Danger</h3>
            <textarea placeholder="Describe the danger..." rows={4}></textarea>
            <div className="modal-actions">
              <button onClick={() => setShowDangerModal(false)}>Cancel</button>
              <button className="send-button" onClick={handleReportDanger}>
                Submit
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
