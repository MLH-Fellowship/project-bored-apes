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
        response = self.client.get("/timeline")

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

    def test_compare_get_and_database(self):
        # Generate information for the timeline post
        name = generate_random_name()
        email = generate_random_email(name)
        content = generate_random_content()

        # Make a POST request
        post_response = self.client.post("/api/timeline_post", data={
            "name": name,
            "email": email,
            "content": content
        })

        # Must return a status code of 200
        self.assertEqual(post_response.status_code, 200)

        # Must be a JSON response
        self.assertTrue(post_response.is_json)

        # Get the id from the POST response
        returned_id = post_response.get_json()['id']

        # Query the database
        queried_timeline_post = TimelinePost.get_by_id(returned_id)

        # Make a GET request
        response = self.client.get("/api/timeline_post")

        # Must return a status code of 200
        self.assertEqual(response.status_code, 200)

        # Must be a JSON response
        self.assertTrue(response.is_json)

        # Parse the JSON response
        get_response = response.get_json()

        # Get the specific timeline post
        get_timeline_post = get_response['timeline_posts'][0]

        # timeline post name from DB must match the timeline post name from GET
        self.assertEqual(queried_timeline_post.name, get_timeline_post['name'])

        # timeline post email from DB must match the timeline post email from GET
        self.assertEqual(queried_timeline_post.email,
                         get_timeline_post['email'])

        # timeline post content from DB must match the timeline post content from GET
        self.assertEqual(queried_timeline_post.content,
                         get_timeline_post['content'])

        # Clear all timeline posts
        self.client.delete("/api/timeline_post")

        def test_post_then_query_database(self):
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

        # id returned by response from POST request
        json = response.get_json()

        # Length of JSON must be greater than 0
        self.assertGreater(len(json), 0)

        # Get the id returned by the POST response
        returned_id = json['id']

        # Query the database
        post = TimelinePost.get_by_id(returned_id)

        # name must be equal to the name in the database
        self.assertEqual(name, post.name)

        # email must be equal to the email in the database
        self.assertEqual(email, post.email)

        # content must be equal to the content in the database
        self.assertEqual(content, post.content)

        # clear all timeline posts
        self.client.delete("/api/timeline_post")
    def test_malformed_timeline_post(self):
        # POST request with missing name
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html
        
        # POST request with empty name
        response = self.client.post("/api/timeline_post", data={
            "name": "",
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with missing content
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world, I'm John"
        })

        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

        # POST request with missing email
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "content": "Hello world, I'm John"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

        # POST request with empty email
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "content": "Hello world, I'm John",
            "email": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html