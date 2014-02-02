import socket
import sys
import itertools
from optparse import OptionParser

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("", 8081))

    value = 1
    while value:
        pin = input("pin")
        value = input("value")
        json = '{"%s": "%s"}' %(pin, value)
        print(json)
        s.send(bytes(json.encode()))
        str(s.recv(1000))

if __name__ == "__main__":
    main()
