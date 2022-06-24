from datetime import datetime
from distutils.text_file import TextFile
from http.client import HTTPResponse
import os
import json

from django.forms import CharField, DateTimeField
from flask import Flask, render_template, request, url_for, redirect, Response
from dotenv import load_dotenv
from .gmail.gmail import send_email
from peewee import *
from playhouse.shortcuts import model_to_dict

import datetime

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                     user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"),
                     host=os.getenv("MYSQL_HOST"),
                     port=3306
                     )

print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])

data = 0
filename = os.path.join(app.static_folder, 'data.json')
with open(filename) as f:
    data = json.load(f)


@app.route("/", defaults={"name": "justin"})
@app.route("/<any(justin):name>", methods=['GET'])
def index(name):
    anchors = ["Experience", "Education", "Projects",
               "Trivia", "Hobbies", "Map", "Contact"]
    return render_template('pages/index.html', title=name, url=os.getenv("URL"), data=data, anchors=anchors)


@app.route("/contact", methods=['POST'])
def contact():
    if request.method == 'POST':
        sender_name = request.form.get("name")
        sender_email = request.form.get("email")
        message = request.form.get("message")
        subject = request.form.get("subject")
        receiver_name = request.form.get("receiver_name")
        receiver_email = request.form.get("receiver_email")
        formatted_message = "Name: {}\nEmail: {}\nMessage: {}".format(
            sender_name, sender_email, message)
        formatted_confirmation = "Hello {},\nYour message for {} has been received.\nThank you.".format(
            sender_name, receiver_name)
        send_email(receiver_name, receiver_email, subject, formatted_message)
        send_email(sender_name, sender_email,
                   "Email Confirmation", formatted_confirmation)
        return '', 204


@app.errorhandler(404)
def page_not_found(e):
    # Set the 404 status explicitly
    return render_template('pages/404.html'), 404


@app.route('/api/timeline_post', methods=['POST'])
def post_timeline_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(
        name=name, email=email, content=content)
    return model_to_dict(timeline_post)


@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_post():
    return {'timeline_posts': [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]}


@app.route('/api/timeline_post/<id>', methods=['GET'])
def get_ids(id):
    try:
        post = TimelinePost.get_by_id(id)
    
    except TimelinePost.DoesNotExist:
        return Response("Timeline post not found", 404)
        
    else:
        return model_to_dict(post)


@app.route('/api/timeline_post/<id>', methods=['DELETE'])
def delete_timeline_post(id):
    TimelinePost.delete_by_id(id)
    # for p in TimelinePost.select():
    #     print(p.id, p.content)
    # return "<p>Hello World</p>"
    return Response("Successfully deleted {}".format(id), 200)


# curl --request POST http://localhost:5000/api/timeline_post -d 'name=Justin&email=justin.monteza@gmail.com&content=Just Added Database to my portfolio site!'

# curl -X POST http://localhost:5000/api/timeline_post -d 'name=Justin&email=justin.monteza@gmail.com&content=Testing my endpoints with postman and curl.'

# curl http://localhost:5000/api/timeline_post