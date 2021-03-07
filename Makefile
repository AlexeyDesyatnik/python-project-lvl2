clean:
	rm -f dist/*

build: clean
	poetry build

install:
	poetry install

publish:
	poetry publish --dry-run

package-install: package-uninstall
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall -y dist/*.whl

gendiff:
	poetry run gendiff



.PHONY:	gendiff