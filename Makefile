install:
	poetry install

clean:
	rm -f dist/*

build: clean
	poetry build

lint:
	poetry run flake8 gendiff

test:
	pytest

publish:
	poetry publish --dry-run

package-install: package-uninstall
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall -y dist/*.whl

gendiff:
	poetry run gendiff



.PHONY:	gendiff test