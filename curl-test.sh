#!/bin/bash
# initial GET request
curl http://localhost:5000/api/timeline_post

# Add timeline_post to database
curl -X POST http://localhost:5000/api/timeline_post -d 'name=Ruy Guzman&email=ruy.guzman2002@gmail.com&content=Testing curl commands'

# GET data with new post
curl http://localhost:5000/api/timeline_post