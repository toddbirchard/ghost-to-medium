from flask import make_response, request
from flask import current_app as app
import requests
from . import r
import json


@app.route('/', methods=['GET'])
def get_user_details():
    """Get details of current user."""
    endpoint = r.get('medium_endpoint_me')
    token = r.get('medium_token')
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8'
    }
    req = requests.get(url=endpoint, headers=headers)
    response = req.content
    print(response)
    return make_response(response, 200)


@app.route('/publish', methods=['POST', 'GET'])
def publish_post():
    """Publish post to Medium."""
    request_data = json.loads(request.data)
    title = request_data['title']
    content = request_data['content']
    tags = request_data['tags']
    token = r.get('medium_token')
    publication = r.get('medium_publication')
    endpoint = 'https://api.medium.com/v1/publications/' + publication + '/posts'
    headers = {
        'Authorization': token,
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
    }
    req = requests.post(url=endpoint, headers=headers, data=json.dumps(data))
    response = req.text
    return make_response(response, 200)
