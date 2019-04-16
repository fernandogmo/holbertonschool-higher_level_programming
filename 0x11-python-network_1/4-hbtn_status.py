#!/usr/bin/python3
''' fetches https://intranet.hbtn.io/status '''
import requests

if __name__ == '__main__':
    status = requests.get('https://intranet.hbtn.io/status')
    print("Body response:",
          "\t- type: {}".format(type(status.text)),
          "\t- content: {}".format(status.text), sep='\n')
