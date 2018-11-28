##Activity 1
A = {'NIM' : 'L200183147',
     'Nama' : 'Nur Annida Iffah Supardi',
     'Alamat' : 'Jl.Bekatung rt 2 rw 2 Desa Telaga Kec.Pelaihari Kab. Tanah Laut Pov. Kalsel',
     'AnakKe' : '2',
     'JumlahSaudara' : '3',
     'TTL' : 'Tanah Laut, 05 Mei 2000',
     'Kewarganegaraan' : 'Indonesia'}

def NIM():
    print (A['NIM'])
def Nama():
    print (A['Nama'])
def Alamat():
    print (A['Alamat'])
def Anakke():
    print (A['Anakke'])
def JumalahSaudara():
    print (A['JumlahSaudara'])
def TTL():
    print (A['TTL'])
def Kewarganegaraan():
    print (A['Kewarganegaraan'])

def r():    
    print(''' Pilihan yang tersedia :
r menampilkan bantuan ini
b menanpilkan NIM
A menampilkan Nama
B menampilkan Alamat
C menampilkan Anak_ke
D menampilkan Jumlah_saudara
E menampilkan TTL
F menampilkan Kewarganegaraan
k keluar''')
r()

while True:
    z = input('Masukkan pilihan saudara: ')
    if z=='r':
        r()
    elif z=='b' :
        NIM()
    elif z=='A':
        Nama()
    elif z=='B':
        Alamat()
    elif z=='C':
        Anak_ke()
    elif z=='D':
       Jumlah_saudara()
    elif z=='E':
        TTL()
    elif z=='F':
        Kewarganegaraan()
    else:
        print('Terima kasih')
        break


