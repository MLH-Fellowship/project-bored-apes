#!/bin/bash

# Change directory
cd project-bored-apes

# Get latest changes from GitHub
git fetch --quiet && git reset origin/main --hard --quiet

# Activate virtual environment
source python3-virtualenv/bin/activate

# Install requirements
pip --quiet install -r requirements.txt

# Reload systemd files
systemctl daemon-reload

# Restart myportfolio service
systemctl restart myportfolio


