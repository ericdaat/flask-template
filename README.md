# Flask Web Application template

This is a template for a basic Flask web application that responds 
an HTML page on `localhost:5000`.

It's pre-configured to run with an SQL database which is [SQLite](https://www.sqlite.org/index.html)
by default, and auto code documentation support using [Sphinx](http://www.sphinx-doc.org/en/master/).

## Install

```
virtualenv venv -p python3;
source venv/bin/activate;
pip install -r requirements.txt
```

## Run
```
FLASK_APP=application flask init-db;
FLASK_APP=application FLASK_DEBUG=True flask run;
```

## Using Docker
If you wish to use Docker for running the app, run the following:

```
docker-compose build;
docker-compose up -d app;
```

## Docs
```
cd docs;
sphinx-apidoc .. -o source;
sphinx-build source build;
open build/index.html;
```
