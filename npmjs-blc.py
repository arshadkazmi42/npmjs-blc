import sys
import requests
import time

from random import randrange


DEBUG = False



# HELPER FUNCTIONS

def _print(text):
    # TODO Add debug / verbose flag / accept from arg
    if DEBUG:
        print(text)


def _get_url_param():

    args = sys.argv

    if len(args) < 2:
        _print('No URL')
        return {}

    return args[1]


def _get_url_result(url):

    response = requests.get(url)

    if response.status_code != 200:
        _print(url)
        _print(f'Failed with error code {response.status_code}')
        _print(str(response.headers))
        if response.status_code == 404:
            print(f'{url} => {response.status_code}')
        
    return response.status_code


# MAIN CODE

url = _get_url_param()
response_code = _get_url_result(url)
_print(f'{url} => {response_code}')
