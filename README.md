# Airdrop-2.0

## Objective
Airdrop-2.0 is intended to be able to send files across internet networks from one device to another.

## Setup
Ultimately, a makefile or .sh file would be best to run and have it execute everything needed. However, for now, loosely follow the following instructions to setup from scratch:
- Ensure the latest version of Python and pip is installed
- Create a project folder: `mkdir airdrop_2.0`, `cd airdrop_2.0`
- Within the project folder, create a virtual environment: `python3 venv airdrop_venv`
- Within the project folder, clone this repo: `git clone <repo_url>`
- Activate the virtual environment (within the project folder airdrop_2.0): `source airdrop_venv/bin/activate`
- Install tqdm: `pip install tqdm`
  
## Database Setup
- Create a Google Sheets API project
- Source venv
-`python3 -m pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib`