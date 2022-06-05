from http.client import HTTPResponse
import os
import re
import json
from tkinter import ANCHOR
from flask import Flask, render_template, request, url_for, redirect, Response
from dotenv import load_dotenv
from .gmail.gmail import send_email

load_dotenv()
app = Flask(__name__)

data = 0
filename = os.path.join(app.static_folder, 'data.json')
with open(filename) as f:
    data = json.load(f)

@app.route("/", defaults={"name": "logan"})
@app.route("/<any(logan, hadi, justin):name>", methods=['GET'])
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
        send_email(receiver_name, receiver_email, subject, formatted_message)
        return '',204


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
