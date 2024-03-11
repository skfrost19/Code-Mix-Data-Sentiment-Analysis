# !/bin/bash

# Create a virtual environment
python3 -m venv codemix

# Activate the virtual environment
source codemix/bin/activate

# Install the required packages
pip install -r requirements.txt

# Run the application
uvicorn webui:app --reload