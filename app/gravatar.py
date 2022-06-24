# import code for encoding urls and generating md5 hashes
import urllib.parse, hashlib

# @app.template_global()
# def get_gravatar_url(email):

# Set your variables here
# email = "justin.monteza@gmail.com"
# default = "https://www.example.com/default.jpg"
# size = 40

# construct the url
#     gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower().encode('utf-8')).hexdigest()
# # gravatar_url += urllib.parse.urlencode({'d':default, 's':str(size)})
#     return gravatar_url

# print(gravatar_url)