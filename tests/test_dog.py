import requests
from jsonschema import validate
import pytest

base_url = "https://dog.ceo/api"


def test_random_dog():
    """DISPLAY SINGLE RANDOM IMAGE FROM ALL DOGS COLLECTION"""
    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            },
            "status": {
                "type": "string"
            }
        },
        "required": ['message', 'status']
    }
    url = base_url + "/breeds/image/random"
    response = requests.get(url)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


@pytest.mark.parametrize("n", [1, 3, 50])
def test_multiple_random_dog(n):
    """DISPLAY MULTIPLE RANDOM IMAGES FROM ALL DOGS COLLECTION"""
    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "array",
                "minItems": 1,
                "maxItems": 50,
                "items": {
                    "type": "string"
                }
            },
            "status": {
                "type": "string"
            }
        },
        "required": ['message', 'status']
    }
    url = base_url + "/breeds/image/random/{}".format(n)
    response = requests.get(url)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


@pytest.mark.parametrize("br", ["hound", "husky", "mountain"])
def test_random_image_from_breed(br):
    """RANDOM IMAGE FROM A BREED COLLECTION"""
    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            },
            "status": {
                "type": "string"
            }
        },
        "required": ['message', 'status']
    }
    url = base_url + "/breed/{}/images/random".format(br)
    response = requests.get(url)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


@pytest.mark.parametrize("sub_br", ["hound", "husky", "mountain"])
def test_sub_breeds(sub_br):
    """LIST ALL SUB-BREEDS"""
    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "status": {
                "type": "string"
            }
        },
        "required": ['message', 'status']
    }
    url = base_url + "/breed/{}/list".format(sub_br)
    response = requests.get(url)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


@pytest.mark.parametrize("sub_br", ["afghan", "basset", "blood"])
def test_random_sub_breeds(sub_br):
    """SINGLE RANDOM IMAGE FROM A SUB BREED COLLECTION"""
    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            },
            "status": {
                "type": "string"
            }
        },
        "required": ['message', 'status']
    }
    url = base_url + "/breed/hound/{}/images/random".format(sub_br)
    response = requests.get(url)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200
