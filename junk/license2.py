import os

def licenseGenerator():
    def encrypt_file():
        bedrijfsnaam = input("Voer bedrijfsnaam in: ")
        maxgebruikers = input("Voer aantal gebruikers in: ")
        Inhoud = "Bedrijfsnaam: " + bedrijfsnaam + "\n Aantal gebruikers: " + maxgebruikers + "\n"
        fileName = input("Benaming van file?: ")+"enc" + ".txt"

        myFile = open(fileName,'a')
        license_text = " Copyright (C) 2019 Free Software Foundation, Inc.  Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed."
        Inhoud = Inhoud.lower().replace(" ", " ")+ "\n" + license_text
        for i in Inhoud:
            myFile.write(chr(ord(i) + 5))

    def decrypt_file():
        fileName = input("Benaming van file?: ")+ "enc" + ".txt"
        with open(fileName,'r+') as f:
            Inhoud = f.read(500)
            for I in Inhoud:
                print(chr(ord(I) - 5), end='')

        Optie = input(" exporteren?: ")
        if Optie == 'ja':
            fileName = input("Nieuwe benaming van file?: ")+"dec" + ".txt"
            myFile = open(fileName,'a')
            Inhoud = Inhoud.lower().replace(" ", " ")
            for i in Inhoud:
                myFile.write(chr(ord(i) - 5))

    def rencrypt_file():
        fileName = input("Benaming van file?: ")+"enc" + ".txt"
        os.startfile(fileName)

    def redecrypt_file():
        fileName = input("Benaming van file?: ")+"dec" + ".txt"
        os.startfile(fileName)

    choice = int(input(
        "1. Toets '1' om encrypted licentie te exporteren.\n2. Toets '2' om licentiebestand te decoderen.\n3. Toets '3' om encrypted licentiebestand te lezen .\n4. Toets '4' om decrypted licentiebestand te lezen .\n5. Press '5' to exit.\n"))

    if choice == 1:
        encrypt_file()
    elif choice == 2:
        decrypt_file()
    elif choice == 3:
        rencrypt_file()
    elif choice ==4:
        redecrypt_file()
    elif choice == 5:
        exit()
    else:
        print("Please select a valid option!")
