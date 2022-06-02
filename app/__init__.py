import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

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



