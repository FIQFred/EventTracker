# Event Tracker System Specification

This document outlines the requirements and features for building a high-performance Event Tracker system.

---

## Overview

The Event Tracker system is designed to ingest, store, and analyze high-frequency IoT event data using a Python FastAPI backend and MongoDB. The system supports asynchronous operations and concurrent ingestion, making it suitable for real-time, large-scale IoT deployments.

---

## Features

### 1. High-Frequency Event Submission

- Accepts high-frequency event submissions (simulating IoT device data) via a Python FastAPI backend.

---

### 2. MongoDB Event Storage

- Stores events in a MongoDB collection with the following schema:
    - `event_id` (unique, string)
    - `device_id` (string)
    - `timestamp` (datetime)
    - `event_type` (string)
    - `payload` (JSON/dict)

---

### 3. CRUD Operations

- **Create:** Accept new events.
- **Read:** Retrieve events by various filters:
    - Device ID
    - Date range
    - Event type
- **Update:** Update an event’s payload or event type.
- **Delete:** Remove an event by ID.

---

### 4. Real-Time Analytics

- Implements analytics using aggregation pipelines or Python logic:
    - **Count events per device.**
    - **Most common event type in the last hour.**

---

### 5. Concurrent Ingestion Simulation

- Write a script that simulates 100 concurrent clients submitting events to the API.
- Includes conflict handling (e.g., rejecting duplicate `event_id`).

---

### 6. Asynchronous Programming

- Uses asynchronous programming:
    - Async FastAPI
    - Async MongoDB driver

---

## Technology Stack

- **Backend:** Python FastAPI (async)
- **Database:** MongoDB (async driver)
- **Simulation:** Python script for concurrent ingestion

---

## Notes

- Ensure unique constraints on `event_id` in MongoDB.
- Use aggregation pipelines for analytics endpoints.
- Design endpoints to handle high concurrency and potential conflicts gracefully.

---
