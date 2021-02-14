# ONEMIND

## TL;DR

  docker-compose up -d
  curl -i

## What is this for

This simple example retrieves periodically (15m by default) forecasting data from _tutiempo.net_, the geo_area queried is configured in_data/list-ES-E41.json_ in the described format. In this example we
get data for all cities in Seville.

The retrieved data is stored in a database (mongodb in this example) and server via a simple rest API, allowing filtering by city.
  GET http://127.0.0.1:5000/forecast?where={"locality.name": "Sevilla"}

## Prerequisites

Docker and docker-compose installed or a local mongodb database.

## Building the images

  docker build -f .\dockerfile_dataretrieval -t dataretrieval .
  docker build -f .\dockerfile_eveapi -t eveapi .
  docker build -f .\dockerfile_testcontainer -t testcontainer .

If you want to use these images instead of the registry ones, you need to properly modify the _docker-compose.yml_ file.

## Tests

There are two test files, they rely on pytest (installed by default in the containers)

- dataRetrieval_test.py
- eveAPI_test.py
  
To test the data retrieving functionality you need to enter the test container and run the tests.
  docker run -it test_container
  cd tests
  pytest dataRetrieval_tests.py

To test the API, you just need to run the code test against your localhost
  pytest eveAPI_tests.py
or use the test container as above.

## Configuring

- If we want to retrieve and store data for a different geo-area, we need to modify the _list-ES-E41.json_ file, included in the data directory. Example files can be found here: <https://api.tutiempo.net/list/>
- In _settings.py_ is the API configuration, including database connection settings, by default, it's configured aim to docker-compose, for a local installation, modify MONGO_HOST for 127.0.0.1
- In _dataretrieval.ini_we can set the database to store data and the datafile source.
