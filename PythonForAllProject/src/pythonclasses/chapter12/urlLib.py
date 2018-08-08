import socket 

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()

# mySocket.connect(('google.com.br', 80))
# cmd = 'GET http://google.com.br HTTP/2.0\n\n'.encode()

mySocket.send(cmd)

while True:
    data = mySocket.recv(512)
    if(len(data) <1):
        break
    print(data.decode())

mySocket.close()