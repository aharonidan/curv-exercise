# Curv Exercise

This repository contains a REST API application that allows to create policy rules for bitcoin transactions.\
The API endpoints are the following.
```
/transactions
/rules
```
Policy rules can include currency, USD or BTC. Whenever a new transaction is added, it is validated against rules in both currencies according to the current BTC/USD exchange rate.

The app is runnnig live on Google Cloud App Engine and can be accessed through the following url.
```
http://silken-order-242812.appspot.com/
```
The app can be used through the auto generated web interface as well as through the json API interface.

## Docker image repository
The live app is running in a docker container. \
The docker image repository can be found in the following url.
```
https://cloud.docker.com/repository/docker/danaharoni1/curv_exercise
```

## Local installation

To install a local copy please clone this repository and run the following commands.\
Create a virtual environment
```
python -m venv env
source env/bin/activate

```
Install dependencies
```
pip install -r requirements.txt
```
Migrate database
```
python run manage.py migrate
```
Run local server
```
python run manage.py runserver
```
Local app will be available at localhost:8000






