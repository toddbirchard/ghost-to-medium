from main import main
import pytest


@pytest.mark.parametrize("main", 'https://hackersandslackers.com/?title=title&content=this is content&url=www.url.com&tags=[fhskjgfgfdg,dfg,df]')
'''def test_main(request_string):
    """Inspect html of incoming page."""
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
    response = req.content
    create_response = {
        'endpoint': endpoint,
        'headers': headers,
        'data': data,
        'response': response
    }
    return create_response'''
