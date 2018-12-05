def encrypt(plaintext: str, sheet: list):
    ciphertext = ""
    for position, character in enumerate(plaintext):
        if character not in Alpha:
            chipertext += character
