from http.client import HTTPResponse
import os
import re
import json
from flask import Flask, render_template, request, url_for, redirect
from dotenv import load_dotenv
from .gmail.gmail import send_email

load_dotenv()
app = Flask(__name__)

data = 0
filename = os.path.join(app.static_folder, 'data.json')
with open(filename) as f:
    data = json.load(f)


@app.route("/<any(logan, hadi, justin):name>")
def index(name):
    anchors = ["Experience", "Projects", "Hobbies", "Map", "Contact"]

    return render_template('index.html', title=name, url=os.getenv("URL"), data=data, anchors=anchors)


@app.route("/contact", methods=['POST'])
def contact():
    if request.method == 'POST':
        sender_name = request.form.get("name")
        sender_email = request.form.get("email")
        message = request.form.get("message")
        subject = request.form.get("subject")

        receiver_name = request.form.get("receiver_name")
        receiver_email = request.form.get("receiver_email")

        formatted_message = "Name: {}\nEmail: {}\nMessage: {}".format(sender_name, sender_email, message)
        
        send_email("Justin Monteza", "justin.monteza@gmail.com", subject, formatted_message)

        return '',204

        # return None

# @app.route('/logan')
# def index():
#     return render_template('index.html', title='logan', url=os.getenv("URL"), data=data)

# @app.route('/hadi')
# def second():
#     return render_template('index.html', title='hadi', url=os.getenv("URL"), data=data)

# @app.route('/justin')
# def third():
#     return render_template('index.html', title='justin', url=os.getenv("URL"), data=data)
