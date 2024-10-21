.PHONY: clean uninstall display run

uninstall:
	rm -rf ~/.el02gm
	rm -rf ~/el02gm

display:
	cat ~/.el02gm/slug.json

clean:
	rm -rf src/gm/__pycache__/

run:
	uv run gm