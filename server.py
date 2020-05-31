import socket

s = socket.socket()  #we can pass two arguments here: 1) IPversion, 2) Type of connection
print('Socket created') 

s.bind(('localhost', 9999))  #s.bind(ipaddress,portnumb)
                           #use portnumber above 2000 since generally they are not occupied

s.listen(3)                 # we are going to serve only upto 3 clients
print('Waiting for connections')

while True:
    c,addr = s.accept()              #s.accept() returrns two values. 1) client soc and 2) address
    name = c.recv(1024).decode()
    print("connected with", addr, name)

    c.send(bytes("Welcome to admantum's house!",'utf-8'))  #The data is to be sent in bytes(utf-8) format  
    c.close()                                              #to close the connection 
