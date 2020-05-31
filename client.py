import socket

c = socket.socket()
#unlike server, we don't need to bind socket with portnumber here    
name = "KT"
c.connect(('localhost',10001))     #passing ipaddr and port_number in binded format
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())               #passing number of bytes to be accepted
                                           #decode() is used to covert bytes to string