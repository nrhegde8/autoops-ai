# 🚀 AutoOps AI — Intelligent Logistics Automation Platform

AutoOps AI is a full-stack, AI-powered logistics automation system designed to simplify operations through intelligent workflows and natural language interaction. It combines a modern React dashboard with a multi-service backend powered by Django and FastAPI, enabling users to manage orders, trigger actions, and automate decisions seamlessly.

---

## 🧠 Overview

AutoOps AI transforms traditional logistics dashboards into an **AI-driven control system**.

Users can:

* Create and manage orders visually
* Interact with an AI assistant using natural language
* Automatically trigger backend workflows (order creation, email sending)
* Route decisions through a dedicated decision engine

This project demonstrates a **microservice-style architecture** with clear separation between UI, AI orchestration, and business logic.

---

## 🏗️ Architecture

```id="arch123"
React Frontend (UI)
        ↓
FastAPI (AI + Tool Executor) — Port 8001
        ↓
Decision Engine (FastAPI) — Port 8002
        ↓
Django REST API (Orders DB) — Port 8000
```

---

## ⚙️ Tech Stack

### Frontend

* React.js (SPA)
* Custom UI system with theming
* Chat-based interaction panel
* Responsive dashboard layout

### Backend

* Django (REST API, database management)
* FastAPI (AI orchestration layer)
* FastAPI (Decision Engine service)

### AI Integration

* Azure OpenAI (GPT-based model)
* Function calling / tool execution pattern

---

## 🚀 Core Features

### 📦 Order Management

* Create orders manually or via chatbot
* Track order status (Pending, In Transit, Delivered)
* Search and filter by product or city

### 🤖 AI Assistant

* Understands natural language
* Executes backend tools automatically

**Examples:**

```id="ex1"
create order for shoes weight 2 in chennai
send email to xyz@gmail.com subject Hello body Test
```

---

### 🧠 Decision Engine (Port 8002)

* Determines courier and priority dynamically
* Decoupled from AI logic for scalability

---

### 📊 Dashboard

* Real-time order statistics
* City-based insights
* Clean card-based UI

---

### ⚙️ Settings & UI

* Theme switching
* Light/Dark mode
* Smooth UX (glass UI, rounded cards)

---

## 📁 Project Structure

```id="struct123"
autoops-ai/
│
├── autoops-frontend/              # React UI
│
├── backend-django/
│   ├── core/
│   │   ├── orders/                # Django models & APIs
│   │   ├── fastapi_service/       # AI + executor (port 8001)
│   │   ├── decision_engine/       # Decision service (port 8002)
│
└── README.md
```

---

## 🛠️ Local Setup

### 1️⃣ Start Django (Port 8000)

```id="run1"
cd backend-django/core
python manage.py runserver
```

---

### 2️⃣ Start AI Service (Port 8001)

```id="run2"
cd backend-django/core/fastapi_service
uvicorn main:app --reload --port 8001
```

---

### 3️⃣ Start Decision Engine (Port 8002)

```id="run3"
cd backend-django/core/decision_engine
uvicorn main:app --reload --port 8002
```

---

### 4️⃣ Start Frontend

```id="run4"
cd autoops-frontend
npm install
npm start
```

---

## 🔐 Environment Variables

Create `.env` inside FastAPI service:

```id="env123"
OPENAI_API_KEY=your_key
AZURE_ENDPOINT=your_endpoint
AZURE_API_VERSION=your_version
DEPLOYMENT_NAME=your_model

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email
EMAIL_PASS=your_app_password
```

---

## 📬 Email Automation

* Triggered via AI tool
* Accepts dynamic recipient input
* Uses SMTP (App Password recommended)
* Fully backend-driven (no frontend exposure)

---

## ⚠️ Important Notes

* Do NOT commit `.env`, `node_modules`, or `db.sqlite3`
* Ensure all 3 services are running simultaneously
* Ports must match configuration (8000, 8001, 8002)

---

## 🌍 Future Enhancements

* Authentication (JWT)
* Real shipment APIs
* Database upgrade (PostgreSQL)
* Deployment (Vercel + Render)
* Role-based access control

---

## 👨‍💻 Author

**Nishanth Hegde**
GitHub: https://github.com/nrhegde8

---

## ⭐ Final Thought

AutoOps AI is a step toward **AI-native applications**, where systems are not just used — they are *interacted with*.
This project demonstrates how conversational interfaces can directly control real backend operations in a scalable architecture.

---
