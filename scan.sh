#!/usr/bin/bash

touch logs.txt
mkdir -p data
touch data/users.csv
touch data/products.csv
touch data/codes.csv
touch data/transactions.csv
if [ ! -d .venv ]; then
	python3 -m venv .venv
fi
source .venv/bin/activate
if ! python3 -m pip freeze | grep -q -F -x -f requirements.txt; then
	pip install -r requirements.txt
fi
python3 src/main.py
deactivate
