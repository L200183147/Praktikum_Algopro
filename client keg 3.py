import socket
hostname = 'localhost'
pesan = ""
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((hostname, 50008))
print"Calculate tube area"
while pesan.lower() !='Quiet':
    pesan = raw_input('Message:')
    s.send(pesan)
    if pesan.lower() !='Quiet':
        response = s.recv(1024)
        print 'Command:',response
    else:
        print"Command:-"
s.close()
