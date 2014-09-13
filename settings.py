#! /usr/bin/python3
import json

default_certfile = '/etc/ssl/pennapps.pem'
default_keyfile = '/etc/ssl/pennapps.key'
default_port = "9999"

def setup():
    data = {}

    print("Input your settings. Default values are listed in [].\n")

    certfile = input("Please enter the location of your server's ca certificate ([{0}]):\n".format(default_certfile))
    if certfile is None or len(certfile) < 1:
        certfile = default_certfile
    data['certfile'] = certfile

    keyfile = input("Please enter the location of your server's ca keyfile [{0}]:\n".format(default_keyfile))
    if keyfile is None or len(keyfile) < 1:
        keyfile = default_keyfile
    data['keyfile'] = keyfile

    port = input("Please enter the port you would like to use [{0}]:\n".format(default_port))
    if port is None or len(port) < 1:
        port = default_port
    data['port'] = int(port)

    with open('settings.json', 'w') as outfile:
        json.dump(data, outfile)

if __name__ == '__main__':
    setup()
