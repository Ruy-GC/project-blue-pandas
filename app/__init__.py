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
#@app.route('/')
#def index():
#     return render_template('index.jinja', 
#          title="MEET THE TEAM!",
#          user1 = data["ruy"],
#          user2 = data["michelle"], 
#          url=os.getenv("URL"))

# Single about page, /<user> allows to get the user value and fectch it from our data.json
@app.route('/')
def homepage():
     return render_template('home.html',
          title = data["ruy"]["name"],
          user_data = data["ruy"],
          url=os.getenv("URL"))

# Education & experience page
@app.route("/ruy/educationexperience")
def education():
     return render_template("education_experience.jinja",
          title = data["ruy"]["name"], 
          majors = data["ruy"]["major"], 
          uni_name = data["ruy"]["school"],
          companies = data["ruy"]["companies"], 
          workexperiences = data["ruy"]["work_experiences"],
          url=os.getenv("URL"))

# Hobbies page
@app.route("/ruy/hobbies")
def hobbies():
     return render_template("hobbies.jinja", 
          title = data["ruy"]["name"], 
          pics = data["ruy"]["hobbies_pics"], 
          hobbies_name = data["ruy"]["hobbies_description"], 
          hobbies_memos = data["ruy"]["hobbies_notes"],
          url=os.getenv("URL"))

# Places page
@app.route("/ruy/places")
def places():
     return render_template("trips.jinja", 
          title = data["ruy"]["name"],
          trips = data["ruy"]["trips"],
          url=os.getenv("URL"),
          API = os.getenv("API"))

@app.route("/ruy/timeline")
def timeline():
     return render_template("timeline.jinja",
          title = data["ruy"]["name"], 
          url=os.getenv("URL"),
     )

@app.errorhandler(404)
def page_not_found(e):
     return render_template('404.html',
          user_data = data["ruy"],
          url=os.getenv("URL"))

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