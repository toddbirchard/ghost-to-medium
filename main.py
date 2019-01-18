from flask import make_response, request
import json
import requests
from requests import Requests
import config


def main(request):
    """From ghost to medium."""
    title = request.form.get('title')
    content = request.form.get('content')
    tags = request.form.get('tags')
    url = request.form.get('url')
    endpoint = 'https://api.medium.com/v1/publications/' + config.publication + '/posts'
    headers = {
        'Authorization': 'Bearer 181d415f34379af07b2c11d144dfbe35d',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8'
    }
    data = {
        "title": title,
        "contentFormat": "html",
        "content": content,
        "tags": tags,
        "publishStatus": "draft",
        "canonicalUrl": url
    }

    prepped = Requests('POST', url=endpoint, headers=headers, data=data)
    req = requests.get(url=endpoint, headers=headers, data=data)
    return make_response(prepped, 200, content_type='application/json')
