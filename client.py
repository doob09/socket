import socket

HOST = '127.0.0.1'
PORT = 7890

#init the socket object for client
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
    #connect to 
    c.connect((HOST,PORT))
    #send data
    c.send(b'this is an echo ')
    #get data
    data = c.recv(1024)

print('Client send and got : ',repr(data))