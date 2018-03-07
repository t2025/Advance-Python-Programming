import socket
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
print("Host name:",host)
port=8090
serversocket.bind((host,port))
serversocket.listen(10)

while True:
    clientsocket,addr=serversocket.accept()
    print("Client-Socket:",clientsocket)
    print("Address:",addr)
    msg="test"
    clientsocket.send(msg.encode('ASCII'))
    
    clientsocket.close()
