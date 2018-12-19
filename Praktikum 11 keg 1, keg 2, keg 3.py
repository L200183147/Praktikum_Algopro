##Kegiatan 1 Show your profile
from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'Personal Data')
my_app.geometry("400x180")

L1 = Label(my_app, text = 'Personal Data' , font = ('Arial' , 22))
L1.grid(row=0 , column=0)
L1.place(x=0, y=0)


L2 = Label(my_app, text = 'Name', font = ('Arial' , 12))
L2.grid(row=1 , column=0)
L2.place(x=0, y=40)
str2 = StringVar(value='Nur Annida Iffah')
E2 = Label (my_app, textvariable=str2)
E2.grid(row=1 , column=1)
E2.place(x=150, y=40)

L3 = Label(my_app , text = 'NIM', font = ('Arial' , 12))
L3.grid(row=2 , column=0)
L3.place(x=0, y=60)
str3 = StringVar(value='L200183147')
E3 = Label(my_app, textvariable=str3)
E3.grid(row=2 , column=1)
E3.place(x=150, y=60)

L4 = Label(my_app, text = 'Favourite Book', font = ('Arial' , 12))
L4.grid(row=3 , column=0)
L4.place(x=0, y=80)
str4 = StringVar(value='Bumi Cinta')
E4 = Label(my_app, textvariable=str4)
E4.grid(row=3, column=1)
E4.place(x=150, y=80)

L5 = Label(my_app , text = 'Idol', font = ('Arial' , 12))
L5.grid(row=4 , column=0)
L5.place(x=0, y=100)
str5 = StringVar(value='Fatimah Az Zahra')
E5 = Label(my_app, textvariable=str5)
E5.grid(row=4 , column=1)
E5.place(x=150, y=100)

L6 = Label(my_app , text = 'Motto', font = ('Arial' , 12))
L6.grid(row=5 , column=0)
L6.place(x=0, y=120)
str6 = StringVar(value='Jangan takut untuk mencoba hal baru')
E6 = Label(my_app, textvariable=str6)
E6.grid(row=5 , column=1)
E6.place(x=150, y=120)


def close():
    my_app.destroy()

B = Button(my_app.quit(), text = 'close' , command = close )
B.grid(row=6 , column=1)
B.place(x=150, y=140)

my_app.mainloop()



## activity 2 Make a simple calculator

from Tkinter import Tk, Label, Entry, Button, StringVar
from Tkinter import LEFT, RIGHT


my_app = Tk(className = 'Calculator')

L1 = Label(my_app, text='First number')
L1.grid(row=0 , column=0 )
str1 = StringVar()
E1 = Entry (my_app, textvariable=str1)
E1.grid(row=0 , column=1 , columnspan=3)
L2 = Label(my_app , text = 'Second number')
L2.grid(row=1 , column=0)
str2 = StringVar()
E2 = Entry(my_app , textvariable=str2)
E2.grid(row=1 , column=1 , columnspan=3)
L3 = Label(my_app , text = 'Result')
L3.grid(row=4 , column=0)
L4 = Label(my_app, text='0')
L4.grid(row=4 , column=2)

def plus ():
    a = float (str1.get())
    b = float (str2.get())
    hasil = a+b
    L4.config(text=hasil)

def minus ():
    c = float (str1.get())
    d = float (str2.get())
    hasil = c-d
    L4.config(text=hasil)

def times ():
    e = float(str1.get())
    f = float (str2.get())
    hasil = e*f
    L4.config(text=hasil)
    
def devide ():
    g = float (str1.get())
    h = float (str2.get())
    hasil = g/h
    L4.config(text=hasil)

B1 = Button (my_app , text = '+' , command = plus)
B1.grid(row=3 , column=0)
B2 = Button (my_app, text= '-' , command = minus)
B2.grid(row=3 , column=1)

B3 = Button (my_app , text = 'x' , command = times)
B3.grid(row=3 , column=2)
B4 = Button (my_app, text= ':' , command = devide)
B4.grid(row=3 , column=3)

my_app.mainloop()


##Activity 3 Calculate the area of the building geometry
from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'Luas Tabung')

L1 = Label(my_app, text = 'Tinggi')
L1.grid(row=0, column=0)
str1 = StringVar( value = 0 )
E1 = Entry(my_app)
E1.grid(row=0 , column=1)

L2 = Label(my_app, text = "Jari-Jari")
L2.grid(row=1, column=0)
str2 = StringVar(value = 1 )
E2 = Entry(my_app)
E2.grid(row=1 , column=1)

L3 = Label(my_app, text = 'Hasil')
L3.grid(row=2 , column=0)

def luas():
    T = float(str1.get())
    R = float(str2.get())
    K = 3,14*R**2
    G = 2*3,14*R*T
    M = 3.14*R**2
    L = (K + G + M)

B1 = Button (my_app, text = 'Hitung Luas' , command = luas)
B1.grid(row=3 , column = 0)

    
str3 = StringVar(value=luas)
E3 = Entry(str3)
E3.grid(row=4, column=0)
