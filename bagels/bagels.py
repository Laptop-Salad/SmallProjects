"""
Bagels
A deductive number guessing game.
Description:
    A user will be prompted to enter a digit between 2-10 (length_num), the length of the number to guess.
    A number with length_num length will be randomly generated.
    The user will have 10 attemps to guess the number and for each guess, there are four possibilities of output:
        "You got it!" - Correct guess (Game ends)
        
        "Fermi x" - How many digits exists and in correct position.
        "Pico x" - How many digits exists not in correct position.
        "Wrong x" - How many wrong digits
        
        "Bagels" - No digits are correct.
        
       "You ran out of guesses." - Game ends
       "The number I though of was x"
    Along with number guesses the user can also supply keywords:
        "hint" - uses up one guess, reveals one letter at random.
        "force" - ends game and reveals number.

"""

from random import randint, randrange

def check_guess(guess: str, number: str) -> str:
    """Check how close a guess is to a (2-10) digit number.

    Args:
        guess (str): A (2-10) digit guess.
        number (str): A randomly generated (2-10) digit number.

    Returns:
        str list:
            "You got it!" - Correct guess
            "Fermi x" - How many digits exists and in correct position.
            "Pico x" - How many digits exists not in correct position.
            "Wrong x" - How many wrong digits
            "Bagels" - No digits are correct.
    """
    answer = []
    
    # Check if guess is correct
    if guess == ''.join(number):
        return "You got it!"

    # Check if each digit is "Pico" or "Fermi"
    pico = fermi = 0
    for i in range(0, len(number)):
        if number[i] == guess[i]:
            answer.append("Fermi")
            fermi += 1
        elif number[i] in guess:
            answer.append("Pico")
            pico += 1

    # No correct digits
    if len(answer) == 0:
        return "Bagels"
    
    # Calculate wrong digits
    wrong = len(number) - (pico + fermi)
    
    answer = ["Fermi {}|".format(fermi), "Pico {}|".format(pico), "Wrong {}|".format(wrong)]

    return ' '.join(answer)

def check_keywords(guess: str, number: str, hints: list[str]) -> list[str]:
    """check guess for keywords

    Args:
        guess (str): A (2-10) digit guess.
        number (str): A randomly generated (2-10) digit number.
        hints (str): Same as number, but elements that have been given as hints are removed.

    Returns:
        str list: Depends on guess
            "force": ["force"]
            "hint": ["hint", hints], hints being hints minus the element given as a hint
            "": If guess has no keywords
    """
    if guess.lower() == "force":
        print(number)
        return ["force"] 
    elif guess.lower() == "hint":
        hint = randrange(0, len(number))
        if len(hints) == 0:
            print("You have used up all your hints")
            return [""]
        else: 
            print("{} is in my guess".format(hints.pop(hint)))
            return ["hint", hints]
    
    return [""]

def start_game():
    """start the bagels game
    """
    
    print("How many digits should the number be (between 2 and 10)")
    length_num = input(">")
    
    # Ensure the input is numeric and within 2 and 10 inclusive
    if not length_num.isnumeric() or not int(length_num) >= 2 or not int(length_num) <= 10:
        print("Please supply a number between 2 and 10 inclusive.")
        return
    
    length_num = int(length_num)
    
    number = []
    
    # Hints keeps track of how many letters have been revealed
    hints = []
    
    # Generate a random length_num digit number
    for i in range(0, length_num):
        num = str(randint(0, 9))
        number.append(num)
        hints.append(num)
        
    # Keep track of guesses  
    guesses = 0
    
    print("I have thought up a {} digit number.".format(length_num))
    print(" You have 10 guesses to get it.")

    # Allow the user 10 guesses
    while guesses < 10:
        print("Guess #{}".format(guesses+1))
        guess = input(">")
        
        # Check if guess is a keyword
        keywords = check_keywords(guess, number, hints)
        
        if keywords[0] == "force":
            return
        elif keywords[0] == "hint":
            hints = keywords[1]
            guesses += 1
        # Input is string but must be numeric and length_num digits
        elif guess.isnumeric() and len(guess) == length_num:
            guesses += 1
            check = check_guess(guess, number)
            print(check)

            if check == "You got it!":
                break
        else:
            print("Please enter using the correct format: A {} digit number.".format(length_num))

    # If the user runs out of guesses tell them the answer
    if guesses == 10:
        print("You ran out of guesses.")
        print("The number I thought of was {}.".format(''.join(number)))

    # Ask if the user wants to play again
    print("Do you want to play again? (yes or no)")
    again = input(">")

    if again.lower() == "yes":
        start_game()
    else:
        print("Thanks for playing!")

def display_instruct():
    """display instructions for bagels game
    """
    print("Bagels, a deductive logic game.")
    print("Idea from Al Sweigart")
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues: ")
    
    print("When I say: \tThat means:")
    print("Pico \t\tOne digit is correct but in the wrong position")
    print("Fermi \t\tOne digit is correct and in the right position")
    print("Bagels \t\tNo digit is correct")

def bagels():
    display_instruct()
    start_game()
    
if __name__ == '__main__':
    bagels()
