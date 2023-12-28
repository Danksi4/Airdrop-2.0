venv:
	sudo apt-get install python3.10-venv
	@echo now create your venv (or source it if already existing) before running `make setup`

setup:
	@echo to install all packages required for the database, cryptography, compression, etc
	sudo apt-get install pip
	python3 -m pip install gpspread oauth2client cryptography tqdm

push:
	git add .
	git commit . -m "Commit"
	git pull
	git push



