[![Powered by Vite](https://img.shields.io/badge/Powered%20by-Vite-646CFF?logo=vite&logoColor=white)](https://vitejs.dev/)
[![FastAPI](https://img.shields.io/badge/Powered_by-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com/)

# HopeLink: AI-Powered Disaster Response & Coordination Platform

SDG Focus: SDG 3 (Good Health & Well-being), SDG 11 (Sustainable Cities & Communities) and SDG 13 (Climate Action)

# Frontend Link
 Live Demo: https://wandile-lab.github.io/HopeLink/

# Backend Link

The HopeLink Disaster Response API is live and accessible here:
https://hopelink-backend3.onrender.com

Docs: https://hopelink-backend3.onrender.com/docs
(Explore endpoints, test the AI model, and view schemas)

Health Check: https://hopelink-backend3.onrender.com/health

Root Message: https://hopelink-backend3.onrender.com/

# Overview
Disasters create chaos—delayed aid, overwhelmed shelters, and fragmented data lead to confusion and vulnerability. HopeLink is an AI-enhanced platform that centralizes disaster response, providing real-time coordination tools, intelligent predictions, and accessible support interfaces for affected communities and responders.

> # Note(AI integration)
> 
> As of 29/07/2025 The backend has been rebuilt and now includes a working AI pipeline for disaster classification.
> 
> While the system is functional, some issues remain. Here's the current state:
> 
> AI pipeline trained and saved using joblib
> Text classification (disaster type and urgency) using predict_proba
> FastAPI backend with real, testable endpoints
> Modular structure for model reuse and separation of concerns
> 
> ⚠️ Minor issues with fallback message logic and model file loading paths
> 
> ⚠️ Model trained on small sample data — not yet optimized for large-scale accuracy (MVP status)

# SDG Alignment

SDG 3: Ensure access to emergency health services and mental health support during and after disasters through coordinated AI-assisted triaging and resource tracking

SDG 11: Promote sustainable and resilient cities through disaster preparedness

SDG 13: Strengthen climate resilience and adaptive capabilities using AI

# AI & Engineering Approach
Core Features
Real-time disaster reporting(Mock)

AI-powered predictions for floods and fires (using placeholder ML logic)

Interactive map with:

Live shelter markers

Simulated danger zones

Optimal evacuation routes

# Backend logic to simulate AI-based aid prioritization

Technical Stack
Frontend: React, Leaflet, MUI, Recharts

Backend: FastAPI (modular APIs)

AI Modules: TensorFlow, Scikit-learn (placeholder simulations)

Mapping & Routing: OpenStreetMap (via Leaflet)

# Engineering Highlights
Automation: Dynamic form intake and aid simulation

Scalability: Micro-modular backend and UI components

Testing: Form validation and logic testing

# Data Sources
Simulated disaster datasets

OpenStreetMap (for shelter and geolocation)

Public emergency APIs (planned integration)

# Deliverables
Codebase: Modular frontend/backend with reusable components

Deployment: Live web prototype with interactive UI

Documentation: Architecture, SDG justification, AI ethics report

# Ethical & Sustainability Practices
Bias Mitigation: Simulated ML includes diverse test cases

Eco-efficiency: Lightweight rendering for low-resource environments

Accessibility: Mobile-friendly design for users in disaster conditions







