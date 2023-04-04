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

def check_keywords(guess: str, number: str, hints: list[str], elem_num: int) -> list[str]:
    """check guess for keywords

    Args:
        guess (str): A (2-10) digit guess.
        number (str): A randomly generated (2-10) digit number.
        hints (str): Same as number, but elements that have been given as hints are removed.
        elem_num (int): What number is currenky being looked at

    Returns:
        str list: Depends on guess
            "force": ["force"]
            "hint": ["hint", hints], hints being hints minus the element given as a hint
            "": If guess has no keywords
    """
    if guess.lower() == "force":
        return ["force"] 
    elif guess.lower() == "hint":
        if len(hints) == 0:
            print("You have used up all your hints")
            return ["hints-none"]
        else: 
            hint = randrange(0, len(number))
            print("Number {}: {} is in my guess".format(elem_num+1, hints.pop(hint)))
            return ["hint", hints]
    
    return [""]

def game_loop(numbers: list[str], hints: list[str], length_num: int, guesses: int):
    """the game loop of the bagels game, allows users 10 guesses

    Args:
        number (list[str]): x amount of randomly generated (2-10) digit number.
        hints (str): Same as number, but elements that have been given as hints are removed.
        length_num (int): The length of the number
        guesses (int): how many guesses have been used
    """
    while guesses < 10:
        print("Guess #{}".format(guesses+1))
        guess = input(">")
        
        guesses += 1
        
        # Check if guess is a keyword
        for i in range(0, len(numbers)):
            keywords = check_keywords(guess, numbers[i], hints[i], i)
            
            if keywords[0] == "force":
                print(numbers)
                for elem in range(0, len(numbers)):
                    print("Number {}: {}".format(elem+1, ''.join(numbers[elem])))
                return
            elif keywords[0] == "hint":
                hints[i] = keywords[1]
            elif keywords[0] == "hints-none":
                pass
            # Input is string but must be numeric and length_num digits
            elif guess.isnumeric() and len(guess) == length_num:
                check = check_guess(guess, numbers[i])
                print("Number {}: {}".format(i, check))

                if check == "You got it!":
                    numbers.pop(i)
                    if len(numbers) == 0:
                        print("You guessed all the numbers, game complete!")
                        end_game(guesses)
                        return
                    break
            else:
                print("Please enter using the correct format: A {} digit number.".format(length_num))
    
    end_game(guesses)

def end_game(guesses):
    # If the user runs out of guesses tell them the answer
    if guesses == 10:
        print("You ran out of guesses.")
        print("The number I thought of was {}.".format(''.join(number)))

    # Ask if the user wants to play again
    print("Do you want to play again? (yes or no)")
    again = input(">")
    
    if again.lower() == "yes":
        init_game()
    else:
        print("Thanks for playing!")


def init_game():
    """start the bagels game
    """
    print("How many numbers to guess should there be")
    print("Example: 1 -> 034, 2 -> 186 789")
    numbers = input(">")
    print("\n")
    
    # Ensure the input is numeric and within 1 and 3 inclusive
    if not numbers.isnumeric() or not int(numbers) >= 1 or not int(numbers) <= 3:
        print("Please supply a number between 1 and 3 inclusive.")
        return
    
    numbers = int(numbers)
    
    print("How many digits should the number be (between 2 and 10)")
    length_num = input(">")
    
    # Ensure the input is numeric and within 2 and 10 inclusive
    if not length_num.isnumeric() or not int(length_num) >= 2 or not int(length_num) <= 10:
        print("Please supply a number between 2 and 10 inclusive.")
        return
    
    length_num = int(length_num)
    
    all_hints = []
    all_numbers = []
    
    # Generate numbers random length_num digit number
    for i in range(0, numbers):
        number = []
        hint = []
        for i in range(0, length_num):
            num = str(randint(0, 9))
            number.append(num)
            hint.append(num)
        
        all_hints.append(hint)
        all_numbers.append(number)
        
    # Keep track of guesses  
    guesses = 0
    
    print("I have thought up {}, {} digit numbers.".format(numbers, length_num))
    print(" You have 10 guesses to get it.")

    # Start game loop
    game_loop(all_numbers, all_hints, length_num, guesses)


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
    print("Bagels \t\tNo digit is correct\n")

def bagels():
    display_instruct()
    init_game()
    
if __name__ == '__main__':
    bagels()
