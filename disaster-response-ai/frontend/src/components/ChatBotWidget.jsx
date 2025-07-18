import React, { useState } from "react";
import { Box, TextField, Button, Typography, Paper } from "@mui/material";

export default function ChatBotWidget() {
  const [messages, setMessages] = useState([
    { text: "Hi! How can I help you today?", fromBot: true },
  ]);
  const [input, setInput] = useState("");

  // Dummy bot reply simulation
  function sendMessage() {
    if (!input.trim()) return;
    setMessages((msgs) => [...msgs, { text: input, fromBot: false }]);
    setInput("");

    // Simulate bot reply
    setTimeout(() => {
      setMessages((msgs) => [
        ...msgs,
        {
          text: "Thanks for reaching out. We're here to assist with disaster updates!",
          fromBot: true,
        },
      ]);
    }, 1000);
  }

  return (
    <Paper sx={{ height: "100%", p: 2, display: "flex", flexDirection: "column" }}>
      <Box
        sx={{
          flexGrow: 1,
          overflowY: "auto",
          mb: 2,
          border: "1px solid #ddd",
          borderRadius: 1,
          p: 1,
        }}
      >
        {messages.map((m, i) => (
          <Typography
            key={i}
            align={m.fromBot ? "left" : "right"}
            sx={{
              backgroundColor: m.fromBot ? "#eee" : "#1976d2",
              color: m.fromBot ? "black" : "white",
              borderRadius: 2,
              p: 1,
              m: 0.5,
              maxWidth: "80%",
              marginLeft: m.fromBot ? 0 : "auto",
            }}
          >
            {m.text}
          </Typography>
        ))}
      </Box>
      <Box component="form" onSubmit={(e) => { e.preventDefault(); sendMessage(); }} sx={{ display: "flex", gap: 1 }}>
        <TextField
          value={input}
          onChange={(e) => setInput(e.target.value)}
          size="small"
          fullWidth
          placeholder="Type your message..."
        />
        <Button variant="contained" onClick={sendMessage}>
          Send
        </Button>
      </Box>
    </Paper>
  );
}
