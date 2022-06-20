#!/bin/bash

# Kill all sessions
tmux kill-server

# Change directory
cd project-bored-apes

# Get latest changes from GitHub
git fetch --quiet && git reset origin/main --hard --quiet

# Activate virtual environment
source python3-virtualenv/bin/activate

# Install requirements
pip --quiet install -r requirements.txt

# Start a new tmux session
tmux new-session -d -s flask-portfolio

# Run flask
tmux send-keys 'flask run --host=0.0.0.0' Enter