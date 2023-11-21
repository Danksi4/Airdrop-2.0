# Airdrop-2.0

## Objective
Airdrop-2.0 is intended to be able to send files across internet networks from one device to another. However, for simplicity's sake, we will build it to send files within the same network.

## Setup
Ultimately, a makefile or .sh file would be best to run and have it execute everything needed. However, for now, loosely follow the following instructions to setup from scratch:
- Ensure the latest version of Python and pip is installed
- Create a project folder: `mkdir airdrop_2.0`, `cd airdrop_2.0`
- Within the project folder, create a virtual environment: `python3 venv airdrop_venv`
- Within the project folder, clone this repo: `git clone <repo_url>`
- Activate the virtual environment (within the project folder airdrop_2.0): `source airdrop_venv/bin/activate`
- Install tqdm: `pip install tqdm`
  
## Database Setup
- Follow the Google Sheets API tutorial, using this installation command `python3 -m pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib`

## Features
The features of our proposed program are as follows:
- Interface our program with a modern GUI
- Store and update all necessary info of customer's computers in a cloud database to streamline the connection between computers
- Allow access from one customer's computer to another if mutually agreed by both customers
- Compress, encrypt, and transmit files between customers
