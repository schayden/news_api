import requests
import json
import secrets

NEWSAPI_KEY = "a7ac1ebf1a434664a5e68a86a3ba80f5"

BASE_URL = 'https://newsapi.org/v2/top-headlines'
params = {'apiKey':secrets.NEWSAPI_KEY,'q': 'New Hampshire'}

response = requests.get(BASE_URL, params)
result = response.json()
articles = result["articles"]
for a in articles:
    print(a['title'], "-", a['source']['name'])





