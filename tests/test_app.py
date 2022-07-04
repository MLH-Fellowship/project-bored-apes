# tests/test_app.py

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
        assert len(json["timeline_posts"]) == 0

        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("head", html)
        self.assertIn('link', html)
        self.assertIn('header', html)

    def test_post(self):

        # Testing POST method of /api/timeline_post

        # Generate information for the timeline post
        name = generate_random_name()
        email = generate_random_email(name)
        content = generate_random_content()

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
        name = generate_random_name()
        email = generate_random_email(name)
        content = generate_random_content()

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

        # Must return a status code of 200
        self.assertEqual(response.status_code, 200)

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
