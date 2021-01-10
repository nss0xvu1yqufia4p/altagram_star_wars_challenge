# Altagram Star Wars Challenge

## Requirements

Create a service project using Python. There should be a method to retrieve a list of all starships from the Star Wars movies, sorted by the hyperdrive rating.

Deliverables: 
* Source code
* Deployment instructions

## Overview

The data was sourced from https://github.com/binxhealth/swapi

The starship data was extracted and processed into a single json file.
The script used to process the data can be found in the resources folder.

The service runs on port 8080 and exposes a REST endpoint at the route /starships

The url parameter "order" can be passed with a value of either "asc" or "desc" to specify the order of the results.

The requirements did not specify how the data should be stored in the backend so I kept it simple by storing the data in a single json file.

### Deployment

A Dockerfile has been included to build the service container.
Alternativly the service can be run using docker-compose by running docker-compose up.

~ DHayes
