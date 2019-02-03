# Flask Web Application template

[![Documentation Status](https://readthedocs.org/projects/flask-template/badge/?version=latest)](https://flask-template.readthedocs.io/en/latest/?badge=latest)
[![CircleCI](https://circleci.com/gh/ericdaat/flask-template.svg?style=svg)](https://circleci.com/gh/ericdaat/flask-template)


This is a template for a basic Flask web application that responds 
an HTML page on `localhost:8080`.

This template comes with support for:
 - [SQLlite database](https://www.sqlite.org/index.html)
 - [Sphinx documentation](http://www.sphinx-doc.org/en/master/)
 - [Twitter Bootstrap](https://getbootstrap.com/)
 - [Font Awesome](https://fontawesome.com/)
 - [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/)
 
Don't hesitate to contribute!

## Install
Create a virtual environment and install the requirements.

```
virtualenv venv -p python3;
source venv/bin/activate;
pip install -r requirements.txt
```

## Run
Init the database and run the application.
```
FLASK_APP=application flask init-db;
FLASK_APP=application FLASK_DEBUG=True flask run;
```

## Using Docker
If you wish to use Docker for deploying the app, run the following:

```
docker-compose build;
docker-compose up -d app;
```

## Docs
Automatically create and build the code documentation using Sphinx.
You can use [Read the Docs](https://readthedocs.org/) to build and host the documentation,
like I did [here](https://flask-template.readthedocs.io/en/latest/).
```
cd docs;
sphinx-apidoc .. -o source;
sphinx-build source build;
open build/index.html;
```
