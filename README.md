# Production Engineering - Week 1 - Portfolio Site

Welcome to the portfolio site for the Blue Pandas team from the Summer 2022 production engineering pod 18!

This portfolio site is the result of the work done during week 1 of the fellowship, developed by:

- [Ruy Guzmán Camacho](https://github.com/Ruy-GC)
- [Michelle Lam](https://github.com/michelellam)

## Goals and Inspiration
The project´s goal is to work as a tool to get to now better the members of a team in a personal and professional way, oriented mainly to be a template for future teams and/or individuals.

The design of the website was inspired by a minimalistic perspective, looking always to show the essential following the philosophy of "less is more".

## Technologies

Flask
- As the main framework

Jinja
- For the creation of web templates that are able to implement python code.

HTML & CSS
- Structure and styling

Other tools used were github for version control and figma for the UI design. 

## Main Challenges
None of the members of the team had used Flask and Jinja before so it became a continuous learning process. 

- How to implement jinja templates and extend from other files
- Understanding how the blocks worked to show diferent information using the same files
- Create a responsive UI to make sure our site looks good in any device

## What we acomplished and learned
We were able to build an portfolio that we're proud of, some of the most important achievements are:

- Implementation of the Google Maps API for the Places page
- Dynamic rendering of the information using data from a JSON and routing parameters
- Proficient collaboration within the team and great comunication
- Being able to quickly learn how to use Flask and Jinja

## Installing and running
### Instalation
``` bash
#windows
python -m venv python3-virtualenv
python3-virtualenv/Scripts/activate 
pip install -r requirements.txt

#linux
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate 
pip install -r requirements.txt
```

### Run
``` bash
python3-virtualenv/Scripts/activate 
flask run
```

## Example of Jinja templates imlementation
In base.jinja you'll have the html setup and multiple blocks for content and other data, this blocks can be implemented in any part of the HTML structure. Fo example to fill th body of the HTML file we can do the following:

``` HTML
...
<body>
    <div> {% block content %} {% endblock %} </div>
</body>
...
```

Then on the file that extends our base.jinja we can set that content.

``` HTML
{% extends "base.jinja" %}

{% block content %}

    <div class = "container">
        <h1 class = "about-title">{{title}}'s background</h1>
        <hr style="border: 2px solid red; background-color: red;"/>

        <h2 class = "w3-center" style = "margin-top:50px;">Education</h2>
        <hr class = "hr_education"></hr>

        <h4 class = "education_margin">{{uni_name}}</h4>
        <h4>Currently studying a major in {{majors}}</h4>

        <h2 class = "education_experience_heading_left w3-center" style = "margin-top:50px;">Work Experiences</h2>
        <hr class = "hr_education"></hr>

            <!-- row layout -->
            <div class = "row" >
            <!-- generates a card for each experience
            {% for wks in companies%}
                <!-- defines column layout -->
                <div class  = "education_experience_columns">
                    <h4 class = "w3-center education_margin">{{companies[wks]}}</h4>
                    <p class = "w3-center"> {{workexperiences[wks]}}</p>
                </div>
            {% endfor %}

            </div>
    </div>

{% endblock%}
```

