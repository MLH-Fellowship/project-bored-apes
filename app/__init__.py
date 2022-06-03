import os
import re
import json
from flask import Flask, render_template, request, url_for, redirect
from dotenv import load_dotenv
# from .gmail.gmail import send_email

load_dotenv()
app = Flask(__name__)

data = 0
filename = os.path.join(app.static_folder, 'data.json')
with open(filename) as f:
    data = json.load(f)

@app.route("/<any(logan, hadi, justin):name>")
def index(name):
    return render_template('index.html', title=name, url=os.getenv("URL"), data=data)
# @app.route('/logan')
# def index():
#     return render_template('index.html', title='logan', url=os.getenv("URL"), data=data)

# @app.route('/hadi')
# def second():
#     return render_template('index.html', title='hadi', url=os.getenv("URL"), data=data)

# @app.route('/justin')
# def third():
#     return render_template('index.html', title='justin', url=os.getenv("URL"), data=data)
