from random import randint

Alpha = "abcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*().,?"

def generate_otp(sheets, length):
    for sheet in range(sheets):
        with open("otp" + str(sheet) + ".txt", "w") as f:
            for i in range(length):
                f.write(str(randint(0,26))+"\n")


def load_sheet(filename: str) -> list:
    """open x file, take each element separated by the newline character and put it into a list labled contents"""
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents


def plain():
    plain_text = input("Please type your message: ")
    return plain_text.lower()


def load_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents


def save_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)
        

def encrypt(plaintext: str, sheet: list):
    ciphertext = ""
    for position, character in enumerate(plaintext):
        if character not in Alpha:
            ciphertext += character
        else:
            encry = (Alpha.index(character) + int(sheet[position])) % 26
            ciphertext += Alpha[encry]
    return ciphertext

def decrypt(cyphertext: str, sheet: list):
    plaintext = ""
    for position, character in enumerate(cyphertext):
        if character not in Alpha:
            ciphertext += character
        else:
            decry = (Alpha.index(character) - int(sheet[position])) % 26
            plaintext += Alpha[decry]
    return plaintext

def menu():
    choices = ["1", "2", "3", "4"]
    choice = "0"
    while True:
        while choice not in choices:
            print("What would you like to do?")
            print("1. Generate one-time pads")
            print("2. Encrypt a message")
            print("3. Decrypt a message")
            print("4. Quit the program")
            choice = input("Please type 1, 2, 3, 4 and press Enter: ")

            if choice == "1":
                sheets = int(input(How many OTPs would you like to make?: ))
                length = int(input(Enter maximum length of random numbers?: ))
