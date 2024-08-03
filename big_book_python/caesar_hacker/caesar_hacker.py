"""
Caesar Hacker

Decrypts a message encrypted with a caesar cipher without a key.
"""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
            decrypted_message.append(" ")
        # If the letter is uppercase, we don't need to convert it to uppercase before searching for it in letters
        elif letter.isupper():
            # If shifting the letter is beyond the length of letters
            if (letters.index(letter) - key) >= len(letters):
                # Find the difference
                remainder = (letters.index(letter) - key) - (len(letters) - 1)
                new_letter = letters[remainder]
            else:
                new_letter = letters[letters.index(letter) - key]
            
            decrypted_message.append(new_letter)
        # If the letter is lowercase, we need to convert it to uppercase before searching for it in letters
        else:
            # If shifting the letter is beyond the length of letters
            if (letters.index(letter.upper()) - key) >= len(letters):
                # Find the difference
                remainder = (letters.index(letter.upper()) - key) - (len(letters))
                new_letter = letters[remainder]
            else:
                new_letter = letters[letters.index(letter.upper()) - key]
                
            decrypted_message.append(new_letter.lower())
        
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

message = input(">")

# Ensure message is valid, only contains letters of the alphabet or spaces
while not check_message(message):
    print("Please ensure message is only letters of the alphabet or spaces.") 
    message = input(">")

# For each key (total 26), decrypt the message
for key in range(0, 25):
    print("Key #{}: {}".format(key, decrypt(key, message)))
