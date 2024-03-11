# Create a virtual environment
python -m venv codemix

# Activate the virtual environment
.\codemix\Scripts\Activate

# Install the required packages
pip install -r requirements.txt

# Run the application
uvicorn webui:app --reload