
import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50009))
print "Communication Program about Servers"
while pesan.lower() != 'quit' :
    pesan = raw_input("Command: ")
    s.send(pesan)
    if pesan.lower() != 'quit':
        response = s.recv(1024)
        print 'Output: ', response
s.close()
