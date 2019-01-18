from flask import make_response, request
import requests
from requests import Request
import os


def main(request):
    """From G   host to Medium."""
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

    # prepped = Request('POST', url=endpoint, headers=headers, data=data)
    # prep = prepped.prepare()
    # print(prep.url, prep.body, prep.headers, prep.method)
    req = requests.post(url=endpoint, headers=headers, data=data)
    response = req.json()
    return response
