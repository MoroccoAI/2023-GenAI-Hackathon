# HyprSol Microservices API

HyprSol backend is powered by FatsApi Microservices, consisting of two main services: Project and Software. Each service must be run separately.

## Introduction

This repository contains the microservices API for the HyprSol backend. The Project and Software services provide distinct functionalities and need to be individually initiated for proper functioning.

**Note: The authentication mechanism implemented in this repository is for demonstration purposes only. All API endpoints are currently public. Ensure proper authentication and authorization mechanisms are implemented for production use.**

## Technologies

The API is built using FastAPI, a modern, fast web framework for building APIs with Python 3.7+. Other technologies and tools include Docker for containerization.

## Folder Code Structure

```
api/
├── project/
│   ├── crud/
│   ├── data/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── Dockerfile
│   ├── main.py
│   └── README.md

├── software/
│   ├── crud/
│   ├── data/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── Dockerfile
│   ├── main.py
│   └── README.md

├── .env.example
├── .gitignore
├── main.py
├── auth.py
├── README.md
└── requirement.txt
```

## Run Locally

To run each service locally, follow these steps:

### Project Service

1. Navigate to the project service directory:
   ```bash
   $ cd api/project/
   ```

2. Install the required dependencies:
   ```bash
   $ pip install -r requirement.txt
   ```

3. Run the service using uvicorn:
   ```bash
   $ uvicorn main:app
   ```

### Software Service

1. Navigate to the software service directory:
   ```bash
   $ cd api/software/
   ```

2. Install the required dependencies:
   ```bash
   $ pip install -r requirement.txt
   ```

3. Run the service using uvicorn:
   ```bash
   $ uvicorn main:app
   ```

Make sure to follow these steps separately for each service to have both Project and Software functionalities running locally.

Feel free to explore the individual README files within each service directory for more detailed information on each service's functionality and usage.