import requests
from jsonschema import validate
import pytest

base_url = "https://api.openbrewerydb.org"


def test_single_brewery():
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "brewery_type": {"type": "string"},
            "street": {"type": "string"},
            "address_2": {"type": ["null", "string", "number"]},
            "address_3": {"type": ["null", "string", "number"]},
            "city": {"type": "string"},
            "state": {"type": "string"},
            "county_province": {"type": ["null", "string"]},
            "postal_code": {"type": "string"},
            "country": {"type": "string"},
            "longitude": {"type": "string"},
            "latitude": {"type": "string"},
            "phone": {"type": "string"},
            "website_url": {"type": "string"},
            "updated_at": {"type": "string"},
            "created_at": {"type": "string"}
        },
        "required": ['id', 'name', 'brewery_type', 'street', 'address_2', 'address_3', 'city', 'state',
                     'postal_code', 'country', 'longitude', 'latitude', 'phone',
                     'website_url', 'updated_at', 'created_at', "county_province"]
    }
    url = base_url + "/breweries/madtree-brewing-cincinnati"
    response = requests.get(url)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


def test_list_breweries():
    schema = {
        "type": "array",
        "items": {
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": ["string", "null"]},
                "address_2": {"type": ["null", "string", "number"]},
                "address_3": {"type": ["null", "string", "number"]},
                "city": {"type": "string"},
                "state": {"type": ["string", "null"]},
                "county_province": {"type": ["null", "string"]},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": ["string", "null"]},
                "latitude": {"type": ["string", "null"]},
                "phone": {"type": ["string", "null"]},
                "website_url": {"type": ["string", "null"]},
                "updated_at": {"type": "string"},
                "created_at": {"type": "string"}
            },
        },
        "required": ['id', 'name', 'brewery_type', 'street', 'address_2', 'address_3', 'city', 'state',
                     'postal_code', 'country', 'longitude', 'latitude', 'phone',
                     'website_url', 'updated_at', 'created_at', "county_province"]
    }
    url = base_url + "/breweries"
    response = requests.get(url)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


def test_random_brewery():
    schema = {
        "type": "array",
        "items": {
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": ["string", "null"]},
                "address_2": {"type": ["null", "string", "number"]},
                "address_3": {"type": ["null", "string", "number"]},
                "city": {"type": "string"},
                "state": {"type": ["string", "null"]},
                "county_province": {"type": ["null", "string"]},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": ["string", "null"]},
                "latitude": {"type": ["string", "null"]},
                "phone": {"type": ["string", "null"]},
                "website_url": {"type": ["string", "null"]},
                "updated_at": {"type": "string"},
                "created_at": {"type": "string"}
            },
        },
        "required": ['id', 'name', 'brewery_type', 'street', 'address_2', 'address_3', 'city', 'state',
                     'postal_code', 'country', 'longitude', 'latitude', 'phone',
                     'website_url', 'updated_at', 'created_at', "county_province"]
    }
    url = base_url + "/breweries"
    response = requests.get(url)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


@pytest.mark.parametrize("search", [3, 5, 7])
def test_search_brewery(search):
    schema = {
        "type": "array",
        "items": {
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": ["string", "null"]},
                "address_2": {"type": ["null", "string", "number"]},
                "address_3": {"type": ["null", "string", "number"]},
                "city": {"type": "string"},
                "state": {"type": ["string", "null"]},
                "county_province": {"type": ["null", "string"]},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": ["string", "null"]},
                "latitude": {"type": ["string", "null"]},
                "phone": {"type": ["string", "null"]},
                "website_url": {"type": ["string", "null"]},
                "updated_at": {"type": "string"},
                "created_at": {"type": "string"}
            },
        },
        "required": ['id', 'name', 'brewery_type', 'street', 'address_2', 'address_3', 'city', 'state',
                     'postal_code', 'country', 'longitude', 'latitude', 'phone',
                     'website_url', 'updated_at', 'created_at', "county_province"]
    }
    url = base_url + "/breweries/search?query={}".format(search)
    response = requests.get(url)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


@pytest.mark.parametrize("search", [1, 10, 15])
def test_autocomplete(search):
    schema = {
        "type": "array",
        "items": {
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
            },
            "minItems": 1,
            "maxItems": 15,
        },
        "required": ['id', 'name']
    }

    url = base_url + "/breweries/autocomplete?query={}".format(search)
    response = requests.get(url)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200
