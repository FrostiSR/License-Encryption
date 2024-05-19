# from pyzbar.pyzbar import decode
# from PIL import Image
#
# decoder = decode(Image.open('hello.png'))
# print(decoder)
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import os

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)

    def licenseGenerator():
        def encrypt_file():
            bedrijfsnaam = input("Voer bedrijfsnaam in: ")
            maxgebruikers = input("Voer aantal gebruikers in: ")
            Inhoud = "Bedrijfsnaam: " + bedrijfsnaam + "\nAantal gebruikers: " + maxgebruikers + "\n"
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

    userName = ['Daniel']
    userPass = ['admin']
    count = 0

    for obj in decodedObjects:

        while count < 3:
            if obj.data == b'hello':
                print("U bent ingelogd!")
                licenseGenerator()
                exit()
                break
            else:
                print("De barcode kan niet gelezen worden!")
                count += 1
                cap.release()

        user_name = input('Enter username:')
        password = input('Enter password:')

        if (user_name == userName[0] and password == userPass[0]):
            licenseGenerator()
            exit()
        else:
            print('foutieve gebruikersnaam/ wachtwoord! Probeer opnieuw!')
            exit()

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
