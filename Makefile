setup:
	sudo apt-get install pip
	sudo apt-get install python3.10-venv
	pip install tqdm
	pip install cryptography

push:
	git add .
	git commit . -m "Commit"
	git push



