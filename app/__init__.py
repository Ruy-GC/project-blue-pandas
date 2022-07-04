from email.policy import default
import os
from flask import Flask, render_template, request,json
from dotenv import load_dotenv
from peewee import * 
from datetime import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()

app = Flask(__name__, template_folder='templates')

data = json.load(open('./app/static/data.json'))

# MySQL database ----------------------------------------------------
if os.getenv('TESTING') == 'true':
    print('Running in test mode')
    mydb = SqliteDatabase ('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306)

print(mydb)

class TimelinePost(Model):
     name = CharField()
     email = CharField()
     content = TextField()
     created_at = DateTimeField(default=datetime.now)

     class Meta:
          database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

# Routing -----------------------------------------------------------
@app.route('/')
def index():
     return render_template('index.jinja', 
          title="MEET THE TEAM!",
          user1 = data["ruy"],
          user2 = data["michelle"], 
          url=os.getenv("URL"))

# Single about page, /<user> allows to get the user value and fectch it from our data.json
@app.route('/<user>')
def homepage(user):
     return render_template('home.jinja',
          title = data[user]["name"],
          user_data = data[user],
          user = user,
          url=os.getenv("URL"))

# Education & experience page
@app.route("/<user>/educationexperience")
def education(user):
     return render_template("education_experience.jinja",
          title = data[user]["name"], 
          majors = data[user]["major"], 
          uni_name = data[user]["school"],
          companies = data[user]["companies"], 
          workexperiences = data[user]["work_experiences"],
          user = user,url=os.getenv("URL"))

# Hobbies page
@app.route("/<user>/hobbies")
def hobbies(user):
     return render_template("hobbies.jinja", 
          title = data[user]["name"], 
          pics = data[user]["hobbies_pics"], 
          hobbies_name = data[user]["hobbies_description"], 
          hobbies_memos = data[user]["hobbies_notes"],
          user = user,url=os.getenv("URL"))

# Places page
@app.route("/<user>/places")
def places(user):
     return render_template("trips.jinja", 
          title = data[user]["name"],
          user = user,
          trips = data[user]["trips"],
          url=os.getenv("URL"),
          API = os.getenv("API"))

@app.route("/<user>/timeline")
def timeline(user):
     return render_template("timeline.jinja",
          title = data[user]["name"], 
          user = user,
          url=os.getenv("URL"),
     )
if __name__ == "__init__":
     app.run(debug = True)

# Endpoints -----------------------------------------------------------

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
     name = request.form.get('name')
     email = request.form.get('email')
     content = request.form.get('content')
     if name == '' or name is None:
          return 'Invalid name', 400
     elif content == '' or content is None:
          return 'Invalid content', 400
     elif email == '' or email is None or '@' not in email:
          return 'Invalid email', 400
     else:
          timeline_post = TimelinePost.create(
               name = name,
               email = email,
               content = content
          )
          return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
     return{
          'timeline_posts': [
               model_to_dict(p)
               for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
          ]
     }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_post():
     id = request.form['id']
     TimelinePost.delete_by_id(id)
     return{
          'timeline_posts': [
               model_to_dict(p)
               for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
          ]
     }