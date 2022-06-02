import os
import re
from flask import Flask, render_template, request, url_for, redirect
from dotenv import load_dotenv
from .gmail.gmail import send_email

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/work')
def work():

    experiences = [
        {
            "location": "San Francisco, California",
            "position": "Software Developer Intern",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Uber_logo_2018.svg/2560px-Uber_logo_2018.svg.png",
            "date": "May 2020 - August 2021",
            "responsibilities": ["Developed performant, scalable and highly available applications using Kotlin, Docker, Apache Ignite", "Managed infrastructure using Terraform, Jenkins, and Ansible.", "Implemented delta query APIs resulting in a 99% decrease in payload and a 32-71% decrease in latency"]
        }, {
            "location": "San Francisco, California",
            "position": "Software Developer Intern",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/2560px-Google_2015_logo.svg.png",
            "date": "May 2020 - August 2021",
            "responsibilities": ["Developed performant, scalable and highly available applications using Kotlin, Docker, Apache Ignite", "Managed infrastructure using Terraform, Jenkins, and Ansible.", "Implemented delta query APIs resulting in a 99% decrease in payload and a 32-71% decrease in latency"]
        }, {
            "location": "San Francisco, California",
            "position": "Software Developer Intern",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Microsoft_logo_%282012%29.svg/2560px-Microsoft_logo_%282012%29.svg.png",
            "date": "May 2020 - August 2022",
            "responsibilities": ["Developed performant, scalable and highly available applications using Kotlin, Docker, Apache Ignite", "Managed infrastructure using Terraform, Jenkins, and Ansible.", "Implemented delta query APIs resulting in a 99% decrease in payload and a 32-71% decrease in latency"]
        },
    ]

    return render_template('work.html', experiences=experiences)


@app.route('/education')
def education():
    schools = [
        {
            "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e8/University_of_Alberta_Logo_%282021%29.svg/2560px-University_of_Alberta_Logo_%282021%29.svg.png",
            "degree": "Bachelor of Science",
            "course": "Computing Science & Economics",
            "favourites": ["Computer Networks", "Database Management Systems", "Operating System Concepts"],
            "campus": "https://www.ualberta.ca/external-relations/media-library/community-relations/photos/12784-06-115-athabasca02.png"
        }, 
        {
            "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/QueensU_Wordmark.svg/2560px-QueensU_Wordmark.svg.png",
            "degree": "Bachelor of Computing (Honours) - BCPH",
            "course": "Computer Science",
            "favourites": ["Artificial Intelligence", "Database Management Systems", "Operating System Concepts"],
            "campus": "https://www.queensu.ca/admission/sites/default/files/assets/20200923_220147458_iOS_1.jpg"
        }
    ]
    return render_template('education.html', schools=schools)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    elif request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        subject = request.form.get("subject")
        
        send_email(name, email, subject, message)

        return redirect(url_for('contact'))

@app.route('/map')
def map():
    return render_template('map.html')

  
@app.route('/hobbies/')
def hobbies():
    hobbies = [
        {
            "image": "https://media.timeout.com/images/105863223/750/422/image.jpg",
            "hobby": "Star Wars"
        }, {
            "image": "https://hips.hearstapps.com/amv-prod-gp.s3.amazonaws.com/gearpatrol/wp-content/uploads/2019/11/Mechanical-Keyboard-Buying-Guide-Gear-Patrol-Feature.jpg?crop=1xw:0.65xh;center,top&resize=1200:*",
            "hobby": "Mechanical Keyboards"
        }, {
            "image": "https://assets-prd.ignimgs.com/2021/12/30/36190303-image-7-1640880187142.png",
            "hobby": "Video Games"
        }
        
    ]
    return render_template('hobbies.html', hobbies=hobbies)




