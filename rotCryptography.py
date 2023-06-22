alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetupper = alphabet.upper()
special = "!@#$%^&*(){,'_}"
numbers = '1234567890'
stringtoprint = ""

def cryptography(message, rotation):
    global stringtoprint
    rotation = rotation
    for letter in message:
        if letter in alphabet:
            if alphabet.index(letter) + rotation > 25:  #check if its a lowercase letter
                newindex = alphabet.index(letter) - rotation
            else:
                newindex = alphabet.index(letter) + rotation
            stringtoprint += alphabet[newindex]
        elif letter in alphabetupper:  #check if its an uppercase letter
            if alphabetupper.index(letter) + rotation > 25:
                newindex = alphabetupper.index(letter) - rotation
            else:
                newindex = alphabetupper.index(letter) + rotation
            stringtoprint += alphabetupper[newindex]
        elif letter in special or numbers:  #check if its a number or special character
            stringtoprint += letter
    print(stringtoprint)


message = input("Enter phrase: ")
rotation = int(input("Enter rotation amount between 1 and 25: "))
while rotation < 1 or rotation > 25:
    rotation = int(input("Enter rotation amount between 1 and 25: "))
cryptography(message,rotation)