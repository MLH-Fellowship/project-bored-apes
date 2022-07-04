# tests/test_app.py

import unittest
import requests
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

        # Length of html must be greater than 0
        self.assertGreater(len(html), 0)

        # Title must match "TyRoyLog Portfolio"
        assert "<title>Justin Monteza's Portfolio</title>" in html
    
    def test_stylesheet_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        # Length of html must be greater than 0
        self.assertGreater(len(html), 0)

        # Title must match "TyRoyLog Portfolio"
        assert '<link rel="stylesheet" href="../static/styles/main.css">' in html
    
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json

    def test_post(self):

        # Testing POST method of /api/timeline_post

        # Generate information for the timeline post
        nameRequest = requests.get("https://api.namefake.com/american/male")
        name = nameRequest.json()['name']
        email =  '_'.join(name.lower().split()) + "@gmail.com" 
        contentRequest = requests.get("https://asdfast.beobit.net/api/")
        content = contentRequest.json()['text']

        response = self.client.post("/api/timeline_post", data={
            "name": name,
            "email": email,
            "content": content
        })

        self.assertEqual(response.status_code, 200)

        
        self.assertTrue(response.is_json)

        
        json = response.get_json()

        
        self.assertGreater(len(json), 0)

        
        self.assertEqual(name, json['name'])

        
        self.assertEqual(email, json['email'])

        
        self.assertEqual(content, json['content'])

        
        self.assertEqual(json['id'], 1)

    def test_timeline_page(self):

        # Generate information for the timeline post
        nameRequest = requests.get("https://api.namefake.com/american/male")
        name = nameRequest.json()['name']
        email =  '_'.join(name.lower().split()) + "@gmail.com" 
        contentRequest = requests.get("https://asdfast.beobit.net/api/")
        content = contentRequest.json()['text']

        # Add a timeline post
        response = self.client.post("/api/timeline_post", data={
            "name": name,
            "email": email,
            "content": content
        })

        # Must return a status code of 200
        self.assertEqual(response.status_code, 200)

        # Must be a JSON response
        self.assertTrue(response.is_json)

        # Check the timeline page using GET
        response = self.client.get("/timeline/")

        # Must be an HTML response
        self.assertEqual(response.mimetype, 'text/html')

        # Get a string representation of the request body
        html = response.get_data(as_text=True)

        # length of HTML must be greater than 0
        self.assertGreater(len(html), 0)

        # name must be in the html page
        self.assertIn(name, html)

        # email must be in the html page
        self.assertIn(email, html)

        # content must be in the html page
        self.assertIn(content, html)

        # clear all timeline posts
        self.client.delete("/api/timeline_post")
