#!/usr/bin/python

import getopt
import os
import sys

import requests

_usage = "Usage: mac.py -m <mac address> -k <api key>"


def get_data(api_key, mac):
    headers = {"X-Authentication-Token": api_key, }

    api_url = "https://api.macaddress.io/v1?output=vendor&search=" + mac
    request_data = requests.get(api_url, headers=headers)
    # convert error codes to friendly error messages
    if request_data.status_code != 200:
        if request_data.status_code == 400:
            print("Access restricted. Enter the correct API key.")
        elif request_data.status_code == 401:
            print("Access restricted. Enter the correct API key.")
        elif request_data.status_code == 402:
            print("Access restricted. Check the credits balance.")
        elif request_data.status_code == 422:
            print("Invalid MAC or OUI address was received.")
        elif request_data.status_code == 429:
            print("Too many requests. Try your call again later.")
        elif request_data.status_code == 500:
            print("Internal server error. Try your call again.")
        else:
            print("An error occurred while calling the API")
        sys.exit()
    return request_data.text


def main(argv):
    api_key = os.getenv('API_KEY')
    mac = ''

    try:
        opts, args = getopt.getopt(argv, "hm:k:", ["help", "mac=", "apiKey="])
    except getopt.GetoptError:
        print(_usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(_usage)
            sys.exit()
        elif opt in ("-m", "--mac"):
            mac = arg
        elif opt in ("-k", "--apiKey"):
            api_key = arg

    if not mac:
        print("mac address is required")
    if not api_key:
        print("api key is required")

    if not mac or not api_key:
        print(_usage)
        sys.exit(2)

    data = get_data(api_key, mac)
    print(data)


if __name__ == "__main__":
    main(sys.argv[1:])
