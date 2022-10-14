import requests
from jsonschema import validate
import pytest

base_url = "https://jsonplaceholder.typicode.com"

photos = {
    'type': 'array',
    'properties': {
        'albumId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'url': {'type': 'string'},
        'thumbnailUrl': {'type': 'string'}
    }
}

posts = {
    'type': 'array',
    'properties': {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'body': {'type': 'string'}
    }
}

albums = {
    'type': 'array',
    'properties': {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'}
    }
}

comments = {
    "type": "array",
    "properties": {
        "postId": {'type': 'number'},
        "id": {'type': 'number'},
        "name": {'type': 'string'},
        "email": {'type': 'string'},
        "body": {'type': 'string'}
    },
    "required": ['postId', 'id', 'name', 'email', 'body']
}

todos = {
    'type': 'array',
    'properties': {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'completed': {'type': 'boolean'}
    },
    "required": ['userId', 'id', 'title', 'completed']
}

users = {
    'type': 'array',
    'properties': {
        'id': {'type': 'number'},
        'name': {'type': 'string'},
        'username': {'type': 'string'},
        'email': {'type': 'string'},
        'address': {
            'type': 'array',
            'properties': {
                'street': {'type': 'string'},
                'suite': {'type': 'string'},
                'city': {'type': 'string'},
                'zipcode': {'type': 'string'},
            }
        }
    }
}

@pytest.mark.parametrize("trace, counters",
                         [('posts', 100),
                          ("comments", 500),
                          ("albums", 100),
                          ("photos", 5000),
                          ("todos", 200),
                          ("users", 10)])
def test_get_resource(trace, counters):
    url = base_url + "/{}".format(trace)
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()[counters-1]["id"] == int(counters)


def test_post_resource():
    body = {
        "title": 'foo',
        "body": 'bar',
        "userId": 1,
    }
    url = base_url + "/posts"
    response = requests.post(url, data=body)
    assert response.status_code == 201
    assert response.json()["id"] == 101


def test_delete():
    url = base_url + "/posts/1"
    response = requests.delete(url)
    assert response.status_code == 200


@pytest.mark.parametrize("trace, smth", [
    ("comments", comments),
    ("photos", photos),
    ("albums", albums),
    ("users", users),
    ("todos", todos),
    ("posts", posts)])
def test_nested_resources(trace, smth):
    url = base_url + "/{}".format(trace, smth)
    response = requests.get(url)
    validate(instance=response.json(), schema=smth)
    assert response.status_code == 200
