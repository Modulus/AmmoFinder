SHELL=/bin/bash
PYTHON_SRC_FOLDER=ammo_finder
.DEFAULT_GOAL) := run
python_files := $(shell find $(PYTHON_SRC_FOLDER)/ -type f -name '*.py')


.PHONY: run
run:
	pipenv run $(PYTHON_SRC_FOLDER)


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
