          ##Activity 1
berkas = open("L200183147", "w")
berkas.write("L200183147" + "\n")
berkas.write("05-05-2000" + "\n")
berkas.write("Nur Annida I'ffah Supardi" + "\n")
berkas.close()
          
##Activity 2
berkas1 = open("L200183147", "r")
NIM = berkas1.readline()
TTL = berkas1.readline()
Nama = berkas1.readline()
berkas1.close()

import shelve
berkas2 = shelve.open('Annida.data')
berkas2['data'] = [NIM, TTL, Nama]
berkas2.close()

##Activity 3
import shelve
berkas3=shelve.open('Annida.data', 'r')
for i in berkas3 ['data']:
    print(i)
berkas3.close()

##Activity 4
import shelve
berkas4 = shelve.open('Annida.data', 'r')
for i in berkas4 ['data']:
    print (i)
berkas4.close()
