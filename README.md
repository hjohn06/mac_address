Author: Howing Wang
Company: Accenture

## Introduction
A script that calls macaddress.io rest endpoint and returns the mac address's vendor company name if available.

## Requirements
- Python 3.7 or later.
- Docker
- Virtualenv (optional)
- macaddress.io account

## Getting Started
Create a macaddress.io account and get an api key.  The api key is not included in the project for security reasons.  

## Running Locally
Local execution is done with python.  If virutalenv is desired, setup a virutal env first.  Skip the pip set if virutalenv is already installed.  Replace environment_name with the name of the environment desired.  
```Shell
pip install virutualenv
virutalenv <environment_name>
source <environment_name>/bin/activate
```

Install required libraries and execute.  Replace the mac_address and api_key with valid values.
```Shell
pip install -r requirements.txt
mac.py -m <mac_address> -k <api_key>
```
The api key may also be exported as an environtment variable and used that way.
```Shell
export API_KEY = <api_key>
mac.py -m <mac_address>
```

## Running in Docker
To build
```Shell
docker build -t mac .
```
To run, replace mac address and api_key
```Shell
docker run -e "mac=<mac_address>" -e "api_key=<api_key>" mac
```

## Resources
https://macaddress.io/api/documentation/making-requests