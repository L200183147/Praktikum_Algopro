##Activity 2
def konversiSuhu(C=0, F=0):
    if C != 0:
        F = int(9/5*C+32)
        print("Suhu", C, "Celcius setara dengan", F, "Fahrenheit")
    elif F != 0:
        C = int(5/9*(F-32))
        print("Suhu", F, "Fahrenheit setara dengan", C, "Celcius")
    elif C != 0 and F != 0:
        F = int(9/5*C+32)
        print("Suhu", C, "Celcius setara dengan", F, "Fahrenheit")
    else:
        F = int(9/5*C+32)
        print("Suhu", C, "Celcius setara dengan", F, "Fahrenheit")
    return
        
        
