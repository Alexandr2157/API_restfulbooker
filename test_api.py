import pytest
import requests


def test_GetBookingIds():
    response = requests.get('https://restful-booker.herokuapp.com/booking')
    assert response.status_code == 200


def test_GetBooking(create_id):
    response = requests.get(f'https://restful-booker.herokuapp.com/booking/{create_id}')
    assert response.status_code == 200
    assert response.json()['firstname'] == 'Jim'


def test_CreateBooking():
    payload = {
    "firstname": " Sylvester ",
    "lastname": "Stallone",
    "totalprice": 1010,
    "depositpaid": 'true',
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
    }
    response = requests.post('https://restful-booker.herokuapp.com/booking', json=payload)
    assert 200 == response.status_code
    assert response.json()['booking']['firstname'] == 'Sylvester'
    assert response.json()['booking']['lastname'] == 'Stallone'


def test_UpdateBooking(create_id, token):
    payload = {
        "firstname": "Santana",
        "lastname": "Carlos",
        "totalprice": 473,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(f'https://restful-booker.herokuapp.com/booking/{create_id}',
                            json=payload,
                            headers={
                                'Content-Type': 'application/json',
                                'Accept': 'application/json',
                                'Cookie': f'{token}',
                                'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
                                     }
                            )
    assert 200 == response.status_code
    assert response.json()['firstname'] == payload['firstname']
    assert response.json()['lastname'] == payload['lastname']


def test_PartialUpdateBooking(create_id, token):
    payload = {
        "firstname": "Chan",
        "lastname": "Jackie ",

            }

    response = requests.patch(f'https://restful-booker.herokuapp.com/booking/{create_id}',
                            json=payload,
                            headers={
                                'Content-Type': 'application/json',
                                'Accept': 'application/json',
                                'Cookie': f'{token}',
                                'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
                                     }
                            )
    assert 200 == response.status_code
    assert response.json()['firstname'] == payload['firstname']
    assert response.json()['lastname'] == payload['lastname']


def test_DeleteBooking(create_id, token):
    response = requests.delete(f'https://restful-booker.herokuapp.com/booking/{create_id}',
                               headers={
                                   'Content-Type': 'application/json',
                                   'Cookie': f'{token}',
                                   'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
                                        }
                               )

    assert response.status_code == 201
    response_get = requests.get(f'https://restful-booker.herokuapp.com/booking/{create_id}')
    assert response_get.status_code == 404


def test_PingHealthCheck():
    response = requests.get('https://restful-booker.herokuapp.com/ping')
    assert response.status_code == 201