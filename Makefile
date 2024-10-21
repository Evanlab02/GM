.PHONY: clean uninstall debug run

clean:
	rm -rf src/gm/__pycache__/

uninstall:
	rm -rf ~/.el02gm
	rm -rf ~/el02gm

debug:
	cat ~/.el02gm/slug.json
	cat ~/.gm/backup/slug.json

run:
	uv run gm

format:
	uv run black src/
	uv run isort src/ --profile black

lint: format
	uv run black --check src/
	uv run isort src/ --check-only --profile black
	uv run flake8 src/ --max-line-length=100
	uv run mypy src/ --strict
