
import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50005))
print "Automatic answering machine is ready"
while pesan.lower() != 'exit' :
    pesan = raw_input("Questions: ")
    s.send(pesan)
    if pesan.lower() != 'exit':
        response = s.recv(1024)
        print 'The answer: ', response
response = s.recv(1024)
print 'The answer: ', response
s.close()
