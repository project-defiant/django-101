VERSION := $(shell grep "version" setup.cfg | cut -f3 -d" ")
.ONESHELL:

install:
	python -m venv .venv
	. .venv/bin/activate
	python -m pip install --upgrade pip
	python -m pip install --upgrade setuptools wheel
	python -m pip install -e .[dev]


clean:
	rm -rf .venv
	rm -rf build
	rm -rf *.egg-info

typecheck:
	. .venv/bin/activate
	mypy ./monthly_challenges

format:
	. .venv/bin/activate
	@isort ./monthly_challenges ./tests
	@black ./monthly_challenges ./tests
	@docformatter --in-place ./monthly_challenges ./tests

lint:
	. .venv/bin/activate
	flake8 ./monthly_challenges
	pylint ./monthly_challenges
	

test:
	. .venv/bin/activate
	pytest -vv -s

changelog:
	. .venv/bin/activate
	towncrier

