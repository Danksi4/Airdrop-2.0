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
- the `make setup` command should install all necessry dependencies
- the database class inside the database module has the following methods:
    - addUser: appends new users to the Google sheet
        - arguments: user name (string), IP address (string)
        - returns: nothing
    - findUser: determines if the username is already in the database
        - returns: True if user already found, False if user not already found
    - getUser: 
        -returns: user's ip address based on username if found, False if no user found
    - sheetDump: prints out all users
- more features to be added to accomodate encryption keys

## Features
The features of our proposed program are as follows:
- Interface our program with a modern GUI
- Store and update all necessary info of customer's computers in a cloud database to streamline the 
    connection between computers
- Allow access from one customer's computer to another if in the same network (should we add security?)
- Compress, encrypt, and transmit files between customers
