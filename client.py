import socket
import sys
import itertools
from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("-s", "--server", dest="server_address", help="Address of the server")
    parser.add_option("-p", "--port", dest="port", help="Port of destination")
    parser.add_option("-j", "--json", dest="json", help="Json test string")

    (options, args) = parser.parse_args()

    if options.server_address is None:
        print("You must to add a server address")
    if options.port is None:
        print("You must to add a port")

    if options.port and options.server_address:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((options.server_address, int(options.port)))
        s.send(options.json.encode())
        str(s.recv(1000))

if __name__ == "__main__":
    main()
