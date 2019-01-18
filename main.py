from flask import make_response, request
import requests
from requests import Request
import os


def main(request):
    """From ghost to medium."""
    title = request.form.get('title')
    content = request.form.get('content')
    tags = request.form.get('tags')
    url = request.form.get('url')
    endpoint = 'https://api.medium.com/v1/publications/' + os.environ.get('publication') + '/posts'
    headers = {
        'Authorization': os.environ.get('token'),
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

    prepped = Request('POST', url=endpoint, headers=headers, data=data)
    req = requests.get(url=endpoint, headers=headers, data=data)
    return make_response(prepped, 200, content_type='application/json')
