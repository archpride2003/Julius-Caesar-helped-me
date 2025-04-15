letters = 'abcdefghijklmnopqrstuvwxyz'

def encryption(plaintext, shiftkey):
    ciphertext = ""
    for char in plaintext:
        char = char.lower()
        if char != ' ':
            index = letters.find(char)
            if index == -1:
                ciphertext += char
            else:
                new_index = (index + shiftkey) % 26  
                ciphertext += letters[new_index]
        else:
            ciphertext += ' '  
    return ciphertext

def decryption(ciphertext, shiftkey):
    plaintext = ""
    for char in ciphertext:
        char = char.lower()
        if char != ' ':
            index = letters.find(char)
            if index == -1:
                plaintext += char
            else:
                new_index = (index - shiftkey) % 26  
                plaintext += letters[new_index]
        else:
            plaintext += ' '  
    return plaintext

while True:
    print("Do you want to encrypt or decrypt?")
    user_input = input("Enter 'e' for encryption or 'd' for decryption and 'exit' for finishing the programe: \n").lower()
    if user_input == "e":
        print("ENCRYPTION MODE SELECTED")
        print()
        text = input("Enter your message: \n")
        key = int(input("Enter the key value: \n"))
        ciphertext = encryption(text, key)
        print("Ciphertext:", ciphertext)
    elif user_input == "d":
        print("DECRYPTION MODE SELECTED")
        print()
        text = input("Enter your message to decrypt: \n")
        key = int(input("Enter the same key used for encryption: \n"))
        plaintext = decryption(text, key)
        print("Plaintext:", plaintext)
    elif user_input == "exit":
        print("goodbye ! have a nice day")
        break
    else:
        print("Invalid choice! Please enter either 'e' and 'd' or 'exit'.")
