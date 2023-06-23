# ==================================================================================================================== #
# Version 2.0.0 of my ROT cipher! Can do full 26 character rotation or singular if you want to get a specific rotation #
# Made by Eric E. Github: https://github.com/EricEsquivel                                                              #
# ==================================================================================================================== #

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetupper = alphabet.upper()
special = "!@#$%^&*(){,'_}"
numbers = "1234567890"
stringtoprint = ""


def full(message):
    global stringtoprint
    rotation = 1
    while rotation <= 26:
        stringtoprint = ""
        print(f"Rotation: {rotation}")
        single(message, rotation)
        rotation +=1
        print(f"    {stringtoprint}")
    print("Full 26 character rotation completed")


def single(message, rotation):
    global stringtoprint
    for letter in message: # for every letter in the message
        if letter in alphabet: # Is the letter in lower case alphabet
            newindex = alphabet.index(letter) + rotation
            if newindex > 25:
                secondindex = newindex - 26
                stringtoprint+=alphabet[secondindex]
            else:
                stringtoprint+=alphabet[newindex]
        elif letter in alphabetupper: # Is the letter in upper case alphabet
            newindex = alphabetupper.index(letter) + rotation
            if newindex > 25:
                secondindex = newindex - 26
                stringtoprint+=alphabetupper[secondindex]
            else:
                stringtoprint+=alphabetupper[newindex]
        elif letter in special or numbers: # Is the letter a special character or number
            stringtoprint += letter


message = input("Enter phrase: ")
fullorsingle = input("full rotation or single rotation of choice? (full/single) ")
match fullorsingle:
    case 'full':
        full(message)
    case 'single':
        rotation = int(input("Enter rotation amount between 1 and 25: "))
        while rotation < 1 or rotation > 25:
            rotation = int(input("Enter rotation amount between 1 and 25: "))
        single(message, rotation)
        print(stringtoprint)
    case other:
        print("Invalid input!")