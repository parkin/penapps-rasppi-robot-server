#! /usr/bin/python3

## Sample client.
## 

import socket, ssl
import json
import argparse
#from pprint import pprint

# get settings
try:
    json_data = open('settings.json')
    settings = json.load(json_data)
    json_data.close()
except IOError:
    raise IOError("settings.json not found. Please run setup-stuff.py")

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", type=str, help="IP address or hostname of the server you want to connect to.", default=socket.gethostname())
parser.add_argument("-p", "--port", type=int, help="Port you want to connect to.", default=int(settings['port']))
args = parser.parse_args()

encoding = 'UTF-8'

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations("pennapps-certificates.crt")

s = socket.socket(socket.AF_INET)
# require a certificate
ssl_sock = context.wrap_socket(s)

print("Connecting to: {0}:{1}".format(args.ip, args.port))
ssl_sock.connect((args.ip, args.port))

#pprint("peer name: {0}".format(ssl_sock.getpeername()))
#pprint("peer cert: {0}".format(ssl_sock.getpeercert()))

for i in range(2):
    msg = "hello! {0}".format(i)
    print("sending: {0}.".format(msg))
    ssl_sock.send(bytes(msg, encoding))

ssl_sock.close()
