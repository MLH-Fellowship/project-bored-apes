cd project-bored-apes
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
systemctl restart myportfolio
