install:
	poetry install

build:
	poetry build

gendiff:
	poetry run gendiff

.PHONY:	gendiff