#!/bin/bash
export PORT=10000  # Force port 10000
gunicorn -b 0.0.0.0:$PORT app:app
