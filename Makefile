SHELL=/bin/bash
PYTHON_SRC_FOLDER=ammo_finder
.DEFAULT_GOAL) := run
git_files := $(shell git ls-tree --name-only -r HEAD)
python_files := $(shell find $(PYTHON_SRC_FOLDER)/ -type f -name '*.py')


.PHONY: run
run:
	pipenv run $(PYTHON_SRC_FOLDER)


.PHONY: install
install: Pipfile Pipfile.lock $(python_files)
	pipenv install
	pipenv run pip install --editable .


.PHONY: test
test: $(git_files)
	$(MAKE) install
	pipenv run pytest


.PHONY: run_linting
run_linting: setup.cfg $(python_files)
	$(MAKE) sort_imports


.PHONY: sort_imports
sort_imports: setup.cfg $(python_files)
	pipenv run isort \
	--recursive \
	--virtual-env $(shell pipenv --venv) \
	--project $(PYTHON_SRC_FOLDER) \
	.
