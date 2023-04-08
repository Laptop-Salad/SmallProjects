import string
from random import randrange

print("""
Blackjack

    Rules:
        Try to get as closeto 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned ot the player.
        The dealer stops hitting at a 17.
""")

class Player:
    def __init__(self, cards: str, sum: int):
        self.cards = [cards]
        self.sum = sum

class Dealer:
    def __init__(self, cards: str, sum: int):
        self.cards = [cards]
        self.sum = sum

"""
Cards type: unkown, clubs, spades, diamond
"""
ascii_cards_type = ["""
 ___ 
|## |
|###|
|_##|
""","""
 ___
|?  |
| ♣ |
|__?|
""","""
 ___
|?  |
| ♥ |
|__?|
""","""
 ___
|?  |
| ♠ |
|__?|
""","""
 ___
|?  |
| ♦ |
|__?|
"""
]

ten_card = """
 ___
|10 |
| ♦ |
|_10|
"""

cards = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards_type = ["Club", "Heart", "Spades", "Diamond"]
deck = []

def display_card(card: list[int] or list[str]) -> str:   
   # Handle double digit card
    if cards[card[0]] == "10":
        split = ten_card.splitlines(True)
        new_card = """"""
        
        for line in split:
            current_line = ""
            for character in line:
                if character in ("♦", "♠", "♥", "♣"):
                    possible_characters = ["♦", "♠", "♥", "♣"]
                    current_line += possible_characters[card[1]]
                else:
                    current_line += character
    else:
        ascii_card = ascii_cards_type[card[1]+1]
        split = ascii_card.splitlines(True)
        new_card = """"""
        
        for line in split:
            current_line = ""
            for character in line:
                if character == "?":
                    current_line += cards[card[0]]
                else:
                    current_line += character
            
            new_card += current_line
    
    return new_card

def display_player(player: Player) -> None:
    lines = ["","","","",""]
    print("PLAYER:", player.sum)
    for card in player.cards:
        split_card = display_card(card).splitlines()
        for i in range(0, 5):
            lines[i] += split_card[i]
    
    for line in lines:
        print(line)
    
    print("\n")
        
def display_dealer(dealer: Dealer, first_hidden=False) -> None:
    lines = ["","","","",""]
    print("DEALER:", dealer.sum)
    for card in dealer.cards:
        if first_hidden is True:
            split_card = ascii_cards_type[0].splitlines()
            first_hidden = False
        else:
            split_card = display_card(card).splitlines()
        for i in range(0, 5):
            lines[i] += split_card[i]
    
    for line in lines:
        print(line)
    
    print("\n")
    
def hit(current_sum: int) -> str and int:
    card = randrange(0, len(cards))
    card_type = randrange(0, len(cards_type))
    
    if card == 0:
        if (current_sum + 11) > 21:
            points = 1
        else:
            points = 11
    elif card > 0 and card < 11:
        points = card
    else:
        points = 10
    
    return [card, card_type], points

def check_win(player: Player, dealer: Dealer, bet: int):
    """
    Rules:
    1. If the players first two cards equal 21, the player wins 1.5 times their bet.
    2. If the player and dealers cards both equal 21, its a draw, the players bet is returned.
    3. If the players cards are greater than 21, the dealer takes their bet.
    4. If the dealers cards are greater than 21, the player gets 2 times their bet.
    5. If the dealers cards are greater than or equal to 17 and the players cards are greater than the dealers cards, the player wins 2 times their bet.
    6. If the dealers cards are greater than or equal to 17 and the players cards are equal to the dealers cards, its a tie and the players bet is returned.
    """
    
    if player.sum == 21 :
        bet = float(bet) * 1.5
        print("You win 1.5 times your bet {}".format(bet))
        display_player(player)
        display_dealer(dealer)
        return "W", bet
    elif player.sum == 21 and dealer.sum == 21:
        print("Its a draw! Bet is returned {}".format(bet))
        display_player(player)
        display_dealer(dealer)
        return "P", bet
    elif player.sum > 21:
        print("You bust. The dealer takes your bet")
        display_player(player)
        display_dealer(dealer)
        return "B", 0
    elif dealer.sum > 21:
        bet *= 2
        print("The dealer busts. You win {}".format(bet))
        display_player(player)
        display_dealer(dealer)
        return "B", bet
    elif  dealer.sum >= 17 and player.sum > dealer.sum:
        bet *= 2
        print("You win twice your bet {}".format(bet))  
        display_player(player)
        display_dealer(dealer)
        return "W", bet
    elif dealer.sum >= 17 and player.sum == dealer.sum:
        print("Its a tie your bet is returned. {}".format(bet))    
        display_player(player)
        display_dealer(dealer)
        return "P", bet
    
    return None

def start_game(bet: int):
    # Give dealer 2 cards
    hit_dealer = hit(0)
    dealer = Dealer(hit_dealer[0], hit_dealer[1])
    
    hit_dealer = hit(dealer.sum)
    dealer.cards.append(hit_dealer[0])
    dealer.sum += hit_dealer[1]
    
    # Display dealer cards with first card hidden
    display_dealer(dealer, True)
    
    # Give player 2 cards
    hit_player = hit(0)
    player = Player(hit_player[0], hit_player[1])
    
    hit_player = hit(player.sum)
    player.cards.append(hit_player[0])
    player.sum += hit_player[1]
    
    display_player(player)
    
    # Check for win
    win = check_win(player, dealer, bet)
    if win is not None: return win[1]
    
    while True:
        print("\n(H)it, (S)tand, (D)ouble down")
        move = input(">")
        
        while move.lower() not in ("h", "s", "d"):
            print("Please ensure your input is valid")
            print("(H)it, (S)tand, (D)ouble down")
            move = input(">")
            
        if move.lower() == "h":
            hit_player = hit(player.sum)
            player.cards.append(hit_player[0])
            player.sum += hit_player[1]
            display_player(player)
        elif move.lower() == "s":
            # dealer reveals card, check wins
            break
        elif move.lower() == "d":
            bet = bet * 2
            print("Your bet has been doubled")
            hit_player = hit(player.sum)
            player.cards.append(hit_player[0])
            player.sum += hit_player[1]
            
            display_player(player)

        win = check_win(player, dealer, bet)
        if win is not None: return win[1]
    
    # The dealer keeps hitting until they reach 17
    while dealer.sum < 17:
        hit_dealer = hit(dealer.sum)
        dealer.cards.append(hit_dealer[0])
        dealer.sum += hit_dealer[1]
    
    # Check to see if anyone has won
    win = check_win(player, dealer, bet)
    if win is not None: return win[1]
    
    """
    Extension of Rules:
    7. When the dealer reaches 17 and is under 21. If the players sum of cards is greater than the dealer, while being under 21, they get twice their bet.
    Otherwise the player loses their bet.
    """
    
    # No need to check is player is under 21 as we already called check_win above
    if player.sum > dealer.sum:
        display_player(player)
        display_dealer(dealer)
        
        bet *= 2
        print("You win twice your bet {}".format(bet))
        return bet
    else:
        display_player(player)
        display_dealer(dealer)
        
        print("You lose your bet")
        return 0

def init_game():
    print("Money: 5000")
    print("How much do you bet (1-5000, or QUIT)")
    bet = input(">")
    if bet.lower() == "quit":
        return
    
    if bet.isnumeric() and (int(bet) >= 1 or int(bet) <= 5000):
        bet = start_game(int(bet))
    else:
        print("Please enter a bet of 1-5000 or QUIT")
        return

if __name__ == '__main__':
    init_game()
