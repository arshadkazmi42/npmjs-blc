import sys
import requests
import time

from random import randrange


DEBUG = True



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


def _check_rate_limit(response):
    if response.status_code == 403:
        if 'X-RateLimit-Reset' in response.headers:
            reset_time = int(response.headers['X-RateLimit-Reset'])
            current_time = int(time.time())
            sleep_time = reset_time - current_time + 1
            _print(f'\n\nGitHub Search API rate limit reached. Sleeping for {sleep_time} seconds.\n\n')
            time.sleep(sleep_time)
            return True
    
    return False


def _get_url_result(url):

    response = requests.get(url)

    if response.status_code != 200:
        _print(url)
        _print(f'Failed with error code {response.status_code}')
        _print(str(response.headers))
        
    return response.status_code


# MAIN CODE

url = _get_url_param()
response_code = _get_url_result(url)
_print(f'{url} => {response_code}')