import os
from flask import Flask, render_template, request,json
from dotenv import load_dotenv

load_dotenv("development.env")
app = Flask(__name__, template_folder='templates')

data = json.load(open('./app/static/data.json'))

@app.route('/')
def index():
    return render_template('index.jinja', title="MEET THE TEAM!",user1 = data["ruy"],user2 = data["michelle"], url=os.getenv("URL"))

# Single about page, /<user> allows to get the user value and fectch it from our data.json
@app.route('/<user>')
def homepage(user):
    return render_template('home.jinja',title = data[user]["name"],user_data = data[user],user = user,url=os.getenv("URL"))

#@app.route ("/")
# Education & experience page
@app.route("/<user>/educationexperience")
def education(user):

     return render_template("education_experience.jinja",  title = data[user]["name"], majors = data[user]["major"], uni_name = data[user]["school"],companies = data[user]["companies"], workexperiences = data[user]["work_experiences"],user = user,url=os.getenv("URL"))

# Hobbies page
@app.route("/<user>/hobbies")
def hobbies(user):

     return render_template("hobbies.jinja", title = data[user]["name"], pics = data[user]["hobbies_pics"], hobbies_name = data[user]["hobbies_description"], hobbies_memos = data[user]["hobbies_notes"],user = user,url=os.getenv("URL"))

# Places page
@app.route("/<user>/places")
def places(user):

     return render_template("trips.jinja", title = data[user]["name"],user = user,trips = data[user]["trips"],url=os.getenv("URL"),API = os.getenv("API"))


if __name__ == "__init__":
     app.run(debug = True)





