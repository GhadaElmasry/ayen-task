# ayen-task
Ayen task that emulates text searching in Medical data and find all similar values of a selected key and the percentage of these similarities.

## Clone Project 
To clone the project you should run the following command:
```shell
git clone git@github.com:GhadaElmasry/ayen-task.git
```

## Setup virtual Env
To create the virtual env you should run the following command:
```shell
virtualenv --python=python3.6 .venv
```
Then, you need to activate it by running the following command:
```shell
source .venv/bin/activate
```

## Install requiments (packages dependencies)
To install all required packages you should run the following command:
```shell
pip install -r requirements/requirements.txt
```

## Run migrations
To run migrations you should run the following command:
```shell
./manage.py migrate
```

## Run server
To run the server run the following command:
```shell
./manage.py runserver
```

## Run UnitTest
To rununit tests run the following command:
```shell
pytest
```

## How to test views

* First view: contains a drop-down list with all keys from the file and a search button 
by check `http://127.0.0.1:8000/medicines`
* Second view: contains simple table to list all of the results.
by check `http://127.0.0.1:8000/medicines/results`

## Run Docker containers
To run docker containers run the following commands:
```shell
docker-compose build
```
and then run up command
```shell
docker-compose up
```

then you can access the project on your local by `http://127.0.0.1:8001`
