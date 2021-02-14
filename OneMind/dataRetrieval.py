#!/usr/bin/env python
import requests
from urllib.parse import urlunsplit, urlencode
import json
from pymongo import MongoClient
import time
import logging
from configparser import ConfigParser

def build_api_url(protocol, baseURL, language, apiKey, format, location):
    """
    Build a url in the format
    {protocol}://{baseURL}/{format}/?lan={language}&apid={apiKey}&lid={location}
    https://api.tutiempo.net/json/?lan=es&apid=awYa4XzaqXa6tOv&lid=3768

    Returns:
    string: Well formed URL
    """
    path = f"/{format}"
    query = urlencode(dict(lan=language, apid=apiKey, lid=location))
    return urlunsplit((protocol, baseURL, path, query, ""))

def query_api(url):
    """
    Make a http get request for an URL

    Parameters:
    url (string): requested URL

    Returns:
    None if error (not 200)
    response body in json body if ok
    """
    resp = requests.get(url)
    if resp.status_code != 200:
        logging.error('Error in API request. Code: '.format(resp.status_code).format(url))
        return None
    else:
        return resp.json()


def populate_geoArea(dataFile, configFile):
    """
    Populate a mongodb instance with the result os multiples queries
    for locations forecasting. It keeps in the database just the latest forecast.

    Parameters:
    datafile (string): File containing a tuple of localities-id in the format {"Name":"Sevilla","ID":1990}
    """
    config = ConfigParser()
    config.read(configFile)
    with open(dataFile) as json_file:
        data = json.load(json_file)
        client = MongoClient(config.get('DATABASE', 'MONGO_HOST'), config.getint('DATABASE', 'MONGO_PORT'))
        db = client[config.get('DATABASE', 'MONGO_DBNAME')]
        
        # naive approach, multithreading could be useful, it depends on interval frequency and DDos flood 
        # source protection
        collection = db[config.get('DATABASE', 'MONGO_COL')]
        for p in data:
            url = build_api_url(config.get('DATARETRIEVAL', 'protocol'), config.get('DATARETRIEVAL', 'baseURL'), config.get('DATARETRIEVAL', 'language'), config.get('DATARETRIEVAL', 'apiKey'), config.get('DATARETRIEVAL', 'format'), str(p['ID']))
            resp = query_api(url)  
            if resp != None:
                collection.delete_one({'locality.name' : p['Name']})  
                collection.insert_one(resp)
        client.close()

    
if __name__ == "__main__":
    config = ConfigParser()
    configFile = './dataRetrieval.ini'
    config.read(configFile)
    logging.info('Getting data every '+ str(config.get('DATARETRIEVAL', 'refreshInterval')) + 'minutes')
    while True:
        populate_geoArea(config.get('DATARETRIEVAL', 'datafile'), configFile)
        logging.info('Data refreshed')
        time.sleep(60*config.getint('DATARETRIEVAL', 'refreshInterval'))