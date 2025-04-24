import requests
url = 'https://webhook.site/...'
name = 'img.jpg'
with open(name, 'rb') as f:
    requests.post(url, files={name: f})
