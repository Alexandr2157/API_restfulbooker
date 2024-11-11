import pytest
import requests



@pytest.fixture()
def create_id():
    payload = {

    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"

    }
    response = requests.post('https://restful-booker.herokuapp.com/booking', json=payload).json()
    return response['bookingid']


@pytest.fixture()
def token():
    payload = {
        "username": "admin",
        "password": "password123"

    }
    response = requests.post('https://restful-booker.herokuapp.com/auth', json=payload)
    return response.json()