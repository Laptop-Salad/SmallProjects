"""
Caesar Cipher
"""

def encrypt(key: int, message: str) -> str:
    """encrypt a message given a key

    Args:
        key (int): key to encrypt message
        message (str): message to encrypt

    Returns:
        str: encrypted message
    """
    if key == 0:
        return message
    
    message = list(message)
    encrypted_message = []
    
    # Shift each letter in the message
    for letter in message:
        # If its a space just add a space
        if letter == " ":
            new_letter = " "
        # If the letter is uppercase, we don't need to convert it to uppercase before searching for it in letters
        elif letter.isupper():
            # If shifting the letter is beyond the length of letters
            if (letters.index(letter) + key) >= len(letters):
                # Find the difference
                remainder = (letters.index(letter) + key) - (len(letters) - 1)
                new_letter = letters[remainder]
            else:
                new_letter = letters[letters.index(letter) + key]
        # If the letter is lowercase, we need to convert it to uppercase before searching for it in letters
        else:
            # If shifting the letter is beyond the length of letters
            if (letters.index(letter.upper()) + key) >= len(letters):
                # Find the difference
                remainder = (letters.index(letter.upper()) + key) - (len(letters))
                new_letter = letters[remainder]
            else:
                new_letter = letters[letters.index(letter.upper()) + key].lower()
                
        encrypted_message.append(new_letter)
        
    return ''.join(encrypted_message)
   
def decrypt(key: int, message: str) -> str:
    """decrypt a message given a key

    Args:
        key (int): key to decrypt message
        message (str): message to decrypt

    Returns:
        str: decrypted message
    """
    if key == 0:
        return message
    
    message = list(message)
    decrypted_message = []
    
    # Shift each letter in the message
    for letter in message:
        # If its a space just add a space
        if letter == " ":
            new_letter = " "
        # If the letter is uppercase, we don't need to convert it to uppercase before searching for it in letters
        elif letter.isupper():
            # If shifting the letter is beyond the length of letters
            if (letters.index(letter) - key) >= len(letters):
                # Find the difference
                remainder = (letters.index(letter) - key) - (len(letters) - 1)
                new_letter = letters[remainder]
            else:
                new_letter = letters[letters.index(letter) - key]
        # If the letter is lowercase, we need to convert it to uppercase before searching for it in letters
        else:
            # If shifting the letter is beyond the length of letters
            if (letters.index(letter.upper()) - key) >= len(letters):
                # Find the difference
                remainder = (letters.index(letter.upper()) - key) - (len(letters))
                new_letter = letters[remainder]
            else:
                new_letter = letters[letters.index(letter.upper()) - key].lower()
                
        decrypted_message.append(new_letter)
        
    return ''.join(decrypted_message)

def check_message(message: str) -> bool:
    """check if a message is valid: only letters and spaces

    Args:
        message (str): message to check for validity

    Returns:
        bool: if message is valid or not
    """
    message = list(message)
    
    # Check each letter in message
    for letter in message:
        if letter.upper() not in letters and letter != " ":
            return False
    
    return True

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Get whether user wants encryption or decryption
print("Do you want to (e)ncrypt or (d)ecrypt?")
answer = input(">")

# Ensure answer is valid
while answer.lower() != "e" and answer.lower() != "d":
    print("Please enter (e) for encryption or (d) for decryption.")
    answer = input(">")

# Get key
print("Please enter the key (0 to 25) to use.")
key = input(">")

# Ensure key is valid
while not key.isnumeric() or int(key) < 0 or int(key) > 25:
    print("Please enter the key (0 to 25) to use.")
    key = input(">")

# Since key is valid convert to int
key = int(key)

# Get message to encrypt/decrypt
if answer.lower() == "e":
    print("Enter message to encrypt.")
else:
    print("Enter message to decrypt.")

message = input(">")

# Ensure message is valid, only contains letters of the alphabet or spaces
while not check_message(message):
    print("Please ensure message is only letters of the alphabet or spaces.") 
    message = input(">")

# Pass key and message to function to be encrypted/decrypted
if answer.lower() == "e":
    print(encrypt(key, message))
else:
    print(decrypt(key, message))
