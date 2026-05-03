#!/bin/bash

echo "Building project..."
python3.12 -m venv venv_build
source venv_build/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
echo "Build complete."
