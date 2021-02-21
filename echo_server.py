import socket

HOST = '127.0.0.1'
PORT = 7890

#use the TCP protocol with self closing
# first arg: the address family - default is AF_INET or ipv4
# second arg: socket type
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    pass 