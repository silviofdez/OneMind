#!/usr/bin/env python
import requests

def test_get_existing_locality_status_code_equals_200():
    resp = requests.get('http://127.0.0.1:5000/forecast?where={"locality.name": "Sevilla"}')
    assert resp.status_code == 200

def test_get_existing_locality_content_type_equals_json():
    resp = requests.get('http://127.0.0.1:5000/forecast?where={"locality.name": "Sevilla"}')
    assert resp.headers["Content-Type"] == "application/json"

def test_get_existing_locality_Sevilla_locality_equals_Sevilla():
    resp = requests.get('http://127.0.0.1:5000/forecast?where={"locality.name": "Sevilla"}')
    resp_body = resp.json()
    assert resp_body['_items'][0]['locality']['name'] == 'Sevilla'

def test_get_non_existing_locality_empty_response():
    resp = requests.get('http://127.0.0.1:5000/forecast?where={"locality.name": "Fantasyland"}')
    resp_body = resp.json()
    assert len(resp_body['_items']) == 0

def test_get_existing_locality_Sevilla_day1_all_data_is_returned():
    resp = requests.get('http://127.0.0.1:5000/forecast?where={"locality.name": "Sevilla"}')
    resp_body = resp.json()
    assert len(resp_body['_items'][0]['day1']) == 14