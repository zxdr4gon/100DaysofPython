
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

caesar_cipher = """
        ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
        a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
        8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
        "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
        '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
                    88             88                                 
                ""             88                                 
                                88                                 
        ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
        a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
        8b         88 88       d8 88       88 8PP""""""" 88          
        "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
        '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
                    88                                             
                    88
    """

print(caesar_cipher)

ask = input("Enter 'e' to encrypt or 'd' to decrypt.\n>>> ").lower()
mode = 'encrypt' if ask == 'e' else 'decrypt'
text = input(f"Enter the text you would like to {mode}.\n>>> ").lower()
shift = int(input("What shift would you like to use? Enter a number.\n>>> "))

def encrypt(text, shift):
    '''Encrpyt any text given to you'''
    result = ''
    for ch in text:
        index = alphabet.index(ch) 
        new_index = (index + shift) % len(alphabet)
        result += alphabet[new_index]
    return result

def decrypt(text, shift):
    result = ''
    for ch in text:
        index = alphabet.index(ch) 
        new_index = (index - shift) % len(alphabet)
        result += alphabet[new_index]
    return result

if mode == 'encrypt':
    msg = encrypt(text, shift)
    print(f"The encrypted text is {msg}")
else:
    msg = decrypt(text, shift)
    print(f"The decrypted text is {msg}")