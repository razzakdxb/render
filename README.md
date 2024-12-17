# Time Service API

## Project Overview
A simple Flask-based microservice that provides current time information.

## Features
- Root endpoint with server time and timezone
- `/time` endpoint returning current time in ISO format

## Local Development Setup
1. Clone the repository
2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Run the application
   ```bash
   python backend/app.py
   ```

## Deployment
Deployed on Render with automatic builds from the main branch.

## Technologies
- Flask
- Python 3.9+
- Gunicorn (Production WSGI Server)
