#!/bin/bash
export PORT=8000  # Force port 10000
gunicorn --b 0.0.0.0:$PORT test_app:app
