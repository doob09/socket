import socket

HOST = '127.0.0.1'
PORT = 7890

#init socket object with self closing
# first arg: the address family - default is AF_INET or ipv4
# second arg:which protocol: SOCK_STREAM is socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #provide spefific one to use based one address family type
    s.bind((HOST,PORT))
    #active listen when request comming it will accept
    s.listen()
    #accept : block and wait -> if client connect to -> return connection object,addr
    conn, addr = s.accept()
    #if there is connection
    with conn:
        print('the ip address from other device is:',addr)
        # conn.send(b'Hi from Server') # connection will close after send()
        #listen for any data from client while connection is established
        while True:
            #data in byptes object
            data = conn.recv(1024)
            if not data:
                break
            #send back to client
            conn.sendall(data)