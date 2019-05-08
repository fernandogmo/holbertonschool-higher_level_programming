#!/usr/bin/python3
'''
TODO description
'''
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        s = ""
    else:
        s = sys.argv[1]
    try:
        response = requests.post('http://0.0.0.0:5000/search_user',
                             data={'q': s})
        if not(response.json()):
            print("No result")
        else:
            print("[{}] {}".format(response.json()['id'], response.json()['name']))
    except ValueError:
        print("Not a valid JSON")
