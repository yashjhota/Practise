install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py

format:
	black *.py

run:
	python wikibot.py

lint:
	pylint --disable=R,C,E1120 *.py
# R recommend C configuration warning
all:
	install lint test
 