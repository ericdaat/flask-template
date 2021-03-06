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

``` bash
make venv/bin/activate
```

Init the database by creating all tables.

``` bash
export DATABASE_URL=sqlite:///../db.sqlite3
export FLASK_APP="application.app"
flask init-db
```

## Run

Run the application debug mode.

``` bash
FLASK_DEBUG=True flask run
```

If you wish to use Docker for deploying the app, run the following:

``` bash
docker-compose up -d
```

## Docs

Automatically create and build the code documentation using Sphinx.
You can use [Read the Docs](https://readthedocs.org/) to build and host the documentation,
like I did [here](https://flask-template.readthedocs.io/en/latest/).

``` bash
make docs
```

## Clone the template to another directory

``` bash
./install.sh /path/to/your/dir
```
