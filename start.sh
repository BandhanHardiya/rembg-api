#!/bin/bash
export PORT=${PORT:-8080}  # Ensure PORT is set
gunicorn -b 0.0.0.0:$PORT app:app
