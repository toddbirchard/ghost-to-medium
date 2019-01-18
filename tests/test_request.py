from flask import request
import pytest
import requests
from . import app


@pytest.mark.parametrize("request_string", 'https://hackersandslackers.com/?title=title&content=this is content&url=www.url.com&tags=[fhskjgfgfdg,dfg,df]')
def test_inspect_html(request_string):
    """Inspect html of incoming page."""
    title = request.form.get('title')
    content = request.form.get('content')
    tags = request.form.get('tags')
    url = request.form.get('url')
    endpoint = 'https://api.medium.com/v1/publications/' + r.get('publication') + '/posts'
    headers = {
        'Authorization': r.get('token'),
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


if __name__ == '__main__':
    pytest.main()
