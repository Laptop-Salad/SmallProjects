"""
Cho-Han

A traditional Japanese dice game. Two six-sided dice are rolled by the 
dealer and the player must guess if the dice total to an even (cho) or 
odd (han) number.
"""

from random import randint

print(
"""
Cho-Han

A traditional Japanese dice game. Two six-sided dice are rolled by the 
dealer and the player must guess if the dice total to an even (cho) or 
odd (han) number.
"""
)

def start_game(bet: int) -> int:
    """start the cho han game

    Args:
        bet (int): how much the player bet

    Returns:
        int: how much the player wins
    """
    print("The dealer swirls the cup and you hear the rattle of dice.")
    print("The dealer slams the cup on the floor, still covering the dice and asks for your bet.")
    
    # Roll the dice
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    
    # Add dice values
    total_dice = dice1 + dice2
    answer = ""
    
    # Check if total_dice is even or odd
    if total_dice % 2 == 0:
        answer = "cho"
    else:
        answer = "han"
    
    
    print("\n\tCHO (even) or HAN (odd)?")
    choice = input(">")
    
    # Ensure input is correct only cho or han
    while choice.lower() != "cho" and choice.lower() != "han":
        print("Please enter a valid input")
        print("\n\tCHO (even) or HAN (odd)?")
        choice = input(">")
    
    # Reveal answer
    print("The dealer lifts the cup to reveal")
    print("{} - {}".format(dice1, dice2))
    
    # Decide if the player wins or loses
    if choice == answer:
        # If the player wins they get 2 x their bet - a 10% fee
        bet *= 2
        print("You win! You take {} mon".format(bet))
        print("The house collects a {} mon fee.".format(bet / 10))
        
        bet -= (bet / 10)
        print("You get {}".format(bet))
    else:
        # If the player loses they get nothing
        bet = 0
        print("You lose! The house takes your {} bet".format(bet))
        print("You get 0")
    
    return bet

    
def init_game(money = 5000):
    """initialise the cho han game

    Args:
        money (int, optional): how much money the player starts with. Defaults to 5000.
    """
    while True:
        print("You have {} mon. How must do you bet? (or QUIT)".format(money))
        bet = input(">")

        while not bet.isnumeric() and bet.lower() != "quit":
            print("Please enter a bet or type QUIT")
            print("You have {} mon".format(bet))
            bet = input(">")

        if bet.lower() == "quit":
            return
        
        while int(bet) < 0 or int(bet) > money:
            print("Please enter a bet of {} or less or type QUIT")
            bet = input(">")
        
        if bet.lower() == "quit":
            return
        
        bet = int(bet)
        
        money -= bet
        money += start_game(bet)
    
if __name__ == '__main__':
    init_game()