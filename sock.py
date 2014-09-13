#! /usr/bin/python3
import socket, ssl
import json

try:
    json_data=open('settings.json')
    settings = json.load(json_data)
    json_data.close()
except IOError:
    print("Please run setup-stuff.py")
    exit(1)

def do_something(connstream, data):
    print("connstream: {0}. \tdata: {1}.".format(connstream, data))
    return True

def deal_with_client(connstream):
    data = connstream.read()
    # null data means the client is finished with us
    while data:
        if not do_something(connstream, data):
             # we'll assume do_something returns False
             # when we're finished with client
             break
        data = connstream.read()
    # finished with client

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(certfile=settings['certfile'], keyfile=settings['keyfile'])

bindsocket = socket.socket()
bindsocket.bind((socket.gethostname(), settings['port']))
bindsocket.listen(5)

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
