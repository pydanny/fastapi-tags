clean:
	ruff format .
	ruff check . --fix
	mypy .

MAKECMDGOALS ?= .	

test:
	@echo "Running with arg: $(filter-out $@,$(MAKECMDGOALS))"
	pytest $(filter-out $@,$(MAKECMDGOALS))

pdb:
	@echo "Running with arg: $(filter-out $@,$(MAKECMDGOALS))"
	pytest --pdb --maxfail=10 --pdbcls=IPython.terminal.debugger:TerminalPdb $(filter-out $@,$(MAKECMDGOALS))

coverage:
	coverage run -m pytest .
	coverage report -m
	coverage html

%:
	@:	

build:
	rm -rf dist
	uv build

publish:
	uv publish -t $UV_PUBLISH_TOKEN

VERSION=v$(shell grep -m 1 version pyproject.toml | tr -s ' ' | tr -d '"' | tr -d "'" | cut -d' ' -f3)

tag:
	echo "Tagging version $(VERSION)"
	git tag -a $(VERSION) -m "Creating version $(VERSION)"
	git push origin $(VERSION)