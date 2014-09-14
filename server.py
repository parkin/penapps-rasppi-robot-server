#! /usr/bin/python
import socket
import argparse
import json
try:
    import SocketServer
except ImportError:
    import socketserver as SocketServer

try:
    json_data=open('settings.json')
    settings = json.load(json_data)
    json_data.close()
except IOError:
    print("Please run setup-stuff.py")
    exit(1)

# get the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", type=str, help="IP address or hostname of the server you want to connect to. Default is the device's current external ip.", default="")
parser.add_argument("-p", "--port", type=int, help="Port you want to connect to. Default is in settings.json.", default=int(settings['port']))
args = parser.parse_args()

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{0} wrote {1}.".format(self.client_address[0], self.data))
        # TODO handle data

# hack to the the pi's external ip
if args.ip is None or len(args.ip) < 1:
    dummy_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dummy_socket.connect(('8.8.8.8', 80))
    host = dummy_socket.getsockname()[0]
    dummy_socket.close()
else:
    host = args.ip

server = SocketServer.TCPServer((host, settings['port']), MyTCPHandler)

print("TCPServer listening at {0}:{1}".format(host, settings['port']))
server.serve_forever()
