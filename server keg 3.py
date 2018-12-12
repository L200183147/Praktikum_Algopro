import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50008))
s.listen(5)
print"The server is ready"
perintah = ""
r=0
t=0
while perintah !='quit':
    
    komm, addr = s.accept()
    while perintah !='quit':
        data = komm.recv(1024).lower().split("=")
        perintah = data[0]
        if perintah == 'quit':
            s.close()
            break
        print 'Message:', perintah
        if len(data) == 2:
            if perintah == 'radius':
                r = int(data[1])
                respon = "recorded of radius"
                komm.send(respon)
            elif perintah == 'high':
                t = int(data[1])
                respon = "recorded of high"
                komm.send(respon)
            else:
                komm.send('message unknown')
        elif perintah == 'calculate':
            L = float(22/7*r*r*t)
            respon = "Area of ​​tube with radius {} and the high {} is {}".format(r,t,L)
            komm.send(respon)
        else:
            komm.send('message unknown')
