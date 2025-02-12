.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  init       to initialize a dev environment"
	@echo "  update     to upload pre-commit hooks and re-install dependencies"
	@echo "  lint       to run linters and link checks"
	@echo "  html       to build the documentation"
	@echo "  clean      clear tox environments and builds"

.PHONY: init
init:
	pip install -U tox pre-commit
	rm -rf .tox
	pre-commit install

.PHONY: update
update:
	pre-commit autoupdate
	$(MAKE) init

.PHONY: html
html:
	tox run -e html

.PHONY: lint
lint:
	tox run -e lint,linkcheck

.PHONY: clean
clean:
	rm -rf _build/*
	rm -rf .tox
