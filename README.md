# AI-Powered Ticket Analysis System (POC)

## Overview

This project is a production-inspired Proof of Concept (POC) that integrates **Zoho Desk** with a **Django REST backend** to build an internal AI-powered ticket analysis system.

The primary objective is to automatically receive newly created support tickets from Zoho Desk, process them locally, and generate AI-assisted recommendations using **Small Language Models (SLMs)** running entirely within the organization's infrastructure.

This project is designed for **enterprise internal use**, where customer data is confidential and should never leave the company's environment.

---

# Objectives

* Integrate Zoho Desk with Django using Webhooks.
* Automatically receive ticket creation events.
* Fetch complete ticket details from Zoho Desk.
* Preprocess ticket content.
* Run inference using locally hosted Small Language Models.
* Generate ticket classification, summaries, and recommendations.
* Return structured AI responses.
* Eventually update Zoho Desk with AI-generated recommendations.

---

# Current Phase

## Phase 1 – Zoho Desk Webhook Integration

### Completed

* Django project setup
* Django REST Framework integration
* Webhook endpoint creation
* ngrok integration for local development
* Zoho Desk webhook configuration
* Workflow rule configuration
* Receiving ticket creation events from Zoho Desk
* Logging incoming webhook payloads

Current flow:

```text
Customer
      │
      ▼
Zoho Desk
      │
      ▼
Workflow Rule
      │
      ▼
Webhook
      │
      ▼
ngrok Tunnel
      │
      ▼
Django REST API
      │
      ▼
Print Incoming Payload
```

---

# Project Architecture

```text
ticket_ai/

│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── webhook/
│   ├── views.py
│   ├── urls.py
│   └── apps.py
│
├── zoho/
│
├── tickets/
│
├── common/
│
├── manage.py
│
├── requirements.txt
│
└── .env
```

---

# Technology Stack

## Backend

* Python 3.12
* Django
* Django REST Framework

## Integration

* Zoho Desk
* Webhooks
* REST APIs

## AI (Upcoming)

* Hugging Face Transformers
* SafeTensors
* ONNX Runtime
* Sentence Transformers
* FAISS
* PostgreSQL

---

# System Workflow

```text
Customer creates ticket

        │

        ▼

Zoho Desk

        │

        ▼

Workflow Rule

        │

        ▼

Webhook

        │

        ▼

ngrok Tunnel

        │

        ▼

Django Webhook Endpoint

        │

        ▼

Extract Ticket Information

        │

        ▼

(Upcoming)

Fetch Complete Ticket

        │

        ▼

AI Pipeline
```

---

# Why Webhooks?

Without webhooks, the backend would continuously poll Zoho Desk asking:

"Has a new ticket been created?"

This approach wastes network resources and increases latency.

Instead, Zoho Desk pushes an event immediately whenever a ticket is created.

Benefits:

* Real-time processing
* Lower API usage
* Lower latency
* Event-driven architecture

---

# Why ngrok?

The Django development server runs locally:

```
http://127.0.0.1:8000
```

This address is only accessible from the local machine.

Zoho Desk operates in the cloud and cannot reach localhost directly.

ngrok creates a secure public tunnel:

```text
Internet

      │

      ▼

https://xxxxx.ngrok-free.dev

      │

      ▼

localhost:8000
```

This allows Zoho Desk to send webhook events directly to the local Django server during development.

---

# Current Django Endpoint

```
POST /api/webhooks/zoho/
```

Responsibilities:

* Receive webhook events
* Log request headers
* Log request body
* Return HTTP 200 OK

Current implementation does **not** perform any AI processing.

---

# Current Request Flow

```text
Ticket Created

      │

      ▼

Zoho Workflow

      │

      ▼

Webhook

      │

      ▼

HTTP POST

      │

      ▼

ngrok

      │

      ▼

Django

      │

      ▼

request.headers

request.data

      │

      ▼

Console Output
```

---

# Upcoming Architecture

The webhook payload will only act as an event notification.

The actual ticket will be retrieved using the Zoho Desk REST API.

Future flow:

```text
Customer creates ticket

        │

        ▼

Zoho Desk

        │

        ▼

Webhook

        │

        ▼

Django

        │

        ▼

Extract Ticket ID

        │

        ▼

Zoho REST API

GET /tickets/{ticketId}

        │

        ▼

Complete Ticket JSON

        │

        ▼

Ticket Preprocessing

        │

        ▼

AI Pipeline

        │

        ▼

Recommendation Engine
```

---

# AI Pipeline (Planned)

1. Ticket Retrieval
2. HTML Cleaning
3. Text Normalization
4. Ticket Classification
5. Summarization
6. Named Entity Recognition
7. Similar Ticket Retrieval
8. AI Recommendation Generation
9. Structured JSON Response

---

# Planned Model Architecture

```text
Hugging Face

      │

      ▼

Download Small Language Model

(Phi-3 Mini / Qwen2.5 / SmolLM)

      │

      ▼

SafeTensors Model

      │

      ▼

Transformers Library

(PyTorch)

      │

      ▼

One-Time ONNX Conversion

      │

      ▼

ONNX Runtime

      │

      ▼

Optimized CPU Inference

      │

      ▼

AI Recommendation Engine
```

---

# Development Roadmap

## Phase 1

* Django setup
* Webhook integration
* Receive ticket events

## Phase 2

* Zoho REST API integration
* Fetch complete ticket

## Phase 3

* Ticket preprocessing

## Phase 4

* Local Small Language Model integration

## Phase 5

* SafeTensors loading

## Phase 6

* ONNX conversion

## Phase 7

* ONNX Runtime inference

## Phase 8

* Ticket classification

## Phase 9

* Ticket summarization

## Phase 10

* Entity extraction

## Phase 11

* Similar ticket retrieval using embeddings

## Phase 12

* AI recommendation engine

## Phase 13

* Update Zoho Desk with AI-generated recommendations

---

# Enterprise Design Principles

This project follows several software engineering principles:

* Separation of Concerns
* Single Responsibility Principle (SRP)
* Layered Architecture
* Service-Oriented Design
* Modular Code Organization
* Environment-based Configuration
* Event-Driven Integration
* Local AI Inference for Data Privacy

---

# Long-Term Goal

Build an enterprise-ready AI assistant that helps support engineers by automatically analyzing incoming support tickets, retrieving similar historical issues, generating concise summaries, identifying key entities, and recommending resolutions—all while keeping customer data securely within the organization's infrastructure.
