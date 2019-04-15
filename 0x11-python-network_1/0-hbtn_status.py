#!/usr/bin/python3
''' fetches https://intranet.hbtn.io/status '''
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as hbtn:
            status = hbtn.read()
    print("Body response:",
          "\t- type: {}".format(type(status)),
          "\t- content: {}".format(status),
          "\t- utf8 content: {}".format(status.decode('utf_8')), sep='\n')
