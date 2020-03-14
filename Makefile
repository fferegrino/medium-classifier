POETRY=poetry
POETRY_RUN=$(POETRY) run

nb-to-py:
	$(POETRY_RUN) jupytext --from ipynb --to py:percent --pre-commit