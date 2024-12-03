install:
	poetry install

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run

gendiff:
	poetry run gendiff

build:
	poetry build

.PHONY: gendiff