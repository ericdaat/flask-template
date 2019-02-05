#!make
SHELL=/bin/bash

install:
	[ -e venv ] && rm -rf venv; \
	virtualenv venv; \
	source venv/bin/activate; \
 	pip install -r requirements.txt; \
 	cp -n credentials.env.dist credentials.env; \
 	docker-compose build; \
	echo "done"; \

start-docker:
	docker-compose up -d app;

start-flask:
	source venv/bin/activate;
	FLASK_APP=application FLASK_DEBUG=True flask run;

stop:
	docker-compose down;

docs:
	cd docs; \
	make clean; \
	find source/*.rst ! -name 'index.rst' -type f -exec rm -f {} +; \
	sphinx-apidoc ../application -o source -M; \
	sphinx-build source build; \
	echo "done";
