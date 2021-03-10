all: test

test:
	python3 -m doctest recursive.py
