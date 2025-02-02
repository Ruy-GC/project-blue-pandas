import unittest
import os

os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200

        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html

    def test_timeline(self):
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        #post and get testing
        response = self.client.post('/api/timeline_post', 
        data = {'name':'Neo', 'email':'neo@gmail.com', 'content': '-looks at you- test test' })
        assert response.status_code == 200

        assert response.is_json
        json = response.get_json()
        assert json['name'] == 'Neo'

        response = self.client.get('/api/timeline_post')
        json = response.get_json()
        assert 'Neo' == json['timeline_posts'][0]['name']


    def test_malformed_timeline_post(self):
          #POST request missing name
        response = self.client.post("/api/timeline_post", data=
        {"email": "John@example.com", "content": "Hello World, I'm John"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        #POST request with empty content
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        #POST request with malformed email 
        response = self.client.post('/api/timeline_post', data=
        {'name': "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html