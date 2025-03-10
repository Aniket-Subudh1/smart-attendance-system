#!/bin/bash

# Set up virtual environment for local development
echo "Setting up virtual environment..."
python -m venv venv
source venv/bin/activate

# Install backend dependencies
echo "Installing backend dependencies..."
pip install -r backend/requirements.txt

# Install frontend dependencies
echo "Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo "Setup complete!"
