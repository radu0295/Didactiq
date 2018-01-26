'''Roll: #123
Reverse a number mathematically (e.g. 12345 → 54321)
'''

print ("Introdu numar natural: ")

while True:
    try:
        numar = int(input())
        break
    except ValueError:
        print ("Fii gigel - introdu numaru ala sa fie natural...")

varIntermed, inversa = int(), int()
translator = len(str(numar)) #i-am zis translator pt ca o sa aiba rolul de a muta ceva mai departe
while numar > 0:
    numar, varIntermed = divmod(numar, 10)
    inversa = inversa + varIntermed*(10**translator)
    translator=translator-1

inversa = int(inversa / 10) #sunt zigan :(

print(f"Numarul invers se este {inversa}")


'''varianta mai usoara

'''
print ("Introdu numar natural: ")

while True:
    try:
        numar = int(input())
        break
    except ValueError:
        print ("Ce-am vorbit??")

numar = str(numar)
numar = numar[::-1]


print(f"Numarul invers se este {numar}")
