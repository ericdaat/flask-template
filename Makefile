#!make
SHELL=/bin/bash

include credentials.env
export $(shell sed 's/=.*//' credentials.env)

install:
	rm -rf venv; \
	virtualenv venv; \
	source venv/bin/activate; \
 	pip install -r requirements.txt; \
 	docker-compose build; \
 	cp -n db-credentials.env.dist db-credentials.env; \
	echo "done"; \

start:
	docker-compose up -d app;

stop:
	docker-compose down;

docs:
	cd docs; \
	make clean; \
	find source/*.rst ! -name 'index.rst' -type f -exec rm -f {} +; \
	sphinx-apidoc ../application -o source -M; \
	sphinx-build source build; \
	echo "done";