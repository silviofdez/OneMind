#!/usr/bin/env python
from OneMind import dataRetrieval, settings
import pytest
from pymongo import MongoClient

@pytest.mark.parametrize('protocol, baseURL, language, apiKey, format, location, finalURL', [
    ('https', 'api.tutiempo.net', 'es', 'awYa4XzaqXa6tOv', 'json', 12077, 'https://api.tutiempo.net/json?lan=es&apid=awYa4XzaqXa6tOv&lid=12077'),
])
def test_build_api_url(protocol, baseURL, language, apiKey, format, location, finalURL):
        assert dataRetrieval.build_api_url(protocol, baseURL, language, apiKey, format , location) == finalURL

@pytest.mark.parametrize('url', [
    ('https://api.tutiempo.net/json?lan=es&apid=awYa4XzaqXa6tOv&lid=12077'),
])
def test_query_api(url):
        assert dataRetrieval.query_api != None

@pytest.mark.parametrize('configFile, dataFile, mongodb_server, mongodb_port, database, col, field, field_value',  [
    ('../OneMind/dataRetrieval.ini', '../data/test.json', 'mongodb', 27017, 'forecast', 'forecast_col', 'locality.name', 'Sevilla'),
])
def test_query_api(configFile, dataFile, mongodb_server, mongodb_port, database, col, field, field_value):
    dataRetrieval.populate_geoArea(dataFile, configFile)
    client = MongoClient(mongodb_server, mongodb_port)
    db = client[database]
    collection = db[col]
    doc = collection.find_one({field : field_value})
    assert doc != None