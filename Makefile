POETRY=poetry
POETRY_RUN=$(POETRY) run

ALL_NOTEBOOKS=$(shell find . -name '*.ipynb' -type f -path **/notebooks/* -not -path **.ipynb_checkpoints/*)
ALL_PY_NOTEBOOKS=$(shell find . -name '*.py' -type f -path **/notebooks/* -not -path **.ipynb_checkpoints/*)
SOURCE_FILES=$(shell find . -name '*.py' -type f -path **/src/* -not -path **/.venv/*)
SOURCES_FOLDER=src

init: add-hooks
	$(POETRY) install
	$(POETRY_RUN) pre-commit install
	$(POETRY_RUN) python -c 'import nltk; nltk.download("stopwords")'

add-hooks:
	cp hooks/pre-push .git/hooks/pre-push
	cp hooks/post-checkout .git/hooks/post-checkout
	chmod +x .git/hooks/post-checkout
	chmod +x .git/hooks/pre-push


nb-to-py:
ifneq ($(ALL_NOTEBOOKS),)
	$(POETRY_RUN) jupytext --from ipynb --to py:percent $(ALL_NOTEBOOKS)
endif

py-to-nb:
ifneq ($(ALL_PY_NOTEBOOKS),)
	$(POETRY_RUN) jupytext --from py:percent --to ipynb $(ALL_PY_NOTEBOOKS)
endif

pre-commit-dvc:
	$(POETRY_RUN) dvc status -q

post-checkout-dvc:
	$(POETRY_RUN) dvc checkout

pre-push-dvc:
	$(POETRY_RUN) dvc push

format:
	$(POETRY_RUN) isort -rc $(SOURCES_FOLDER)
	$(POETRY_RUN) black $(SOURCE_FILES)

lint:
	$(POETRY_RUN) isort -rc $(SOURCES_FOLDER) --check-only
	$(POETRY_RUN) black $(SOURCE_FILES) --check