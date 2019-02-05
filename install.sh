#!/bin/bash

# usage: ./install.sh /path/to/dir

rsync -av . "$1" \
	--exclude venv \
	--exclude .git \
	--exclude docs/build \
	--exclude __pycache__ \
	--exclude instance \
	--exclude .idea \
	--exclude .pytest_cache \
	--exclude install.sh