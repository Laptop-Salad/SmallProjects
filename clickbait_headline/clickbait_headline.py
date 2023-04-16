"""
Clickbait Headline Generator

Randomly Generate Clickbait Headlines
"""

from random import sample, randint

pronouns = ["Him", "Her", "Them"]
establishments = ["Companies", "Banks", "Doctors", "Airlines"]
figures = ["Dog", "Cat", "Pensioner", "Fisherman", "Banker", "Cyclist"]
tasks = ["Invented", "Saved", "Shut Down", "Went From"]
superiors = ["Faster", "Cheaper", "Unique", "Softer", "Superior", "Cleaner"]
objects = ["Vacuum Cleaner", "Car", "Massage Chair", "Computer", "Mirror", "Fridge", "Pencil", "Clock", "Sweater", "Coffee Maker", "Oven", "Currency"]
opposites = [
    ["Poor", "Mega Rich"],
    ["Intern", "CEO"],
    ["Banker", "Bank Robber"]
]

def generate_accomplishment(tense):
    """
    Examples:
        - Invented:
            - Invented A Faster Computer
            - Inventer A Softer Sweater
            
        - Saved:
            - Saved £300 In 2 Weeks
            
        - Shut Down:
            - Shut Down Big Airlines
            - Shut Down Big Banks
            
        - Went From:
            - Went From Intern to CEO
            - Went From Poor to Mega Rich
    """
    task = sample(tasks, 1)[0]
    
    match task:
        case "Invented":
            if tense == "past":
                return "Invented a {superior} {obj}".format(
                    superior = sample(superiors, 1)[0],
                    obj = sample(objects, 1)[0]
                )
            else:
                return "Invent a {superior} {obj}".format(
                    superior = sample(superiors, 1)[0],
                    obj = sample(objects, 1)[0]
                )
        case "Saved":
            if tense == "past":
                return "Saved £{money} in {week} Weeks".format(
                    money = randint(1, 10000),
                    week = randint(2, 10)
                )
            else:
                return "Save £{money} in {week} Weeks".format(
                    money = randint(1, 10000),
                    week = randint(2, 10)
                )
        case "Shut Down":
            return "Shut Down Big {establishment}".format(
                establishment = sample(establishments, 1)[0]
            )
        case "Went From":
            opposite = sample(opposites, 1)[0]
            
            if tense == "past":
                return "Went From {opposite_first} to {opposite_second}".format(
                    opposite_first = opposite[0],
                    opposite_second = opposite[1]
                )
            else:
                return "Go From {opposite_first} to {opposite_second}".format(
                    opposite_first = opposite[0],
                    opposite_second = opposite[1]
                )
        case _:
            if tense == "past":
                return "Robbed 6,000,000 People"
            else:
                return "Rob 6,000,000 People"

def generate_establishments_hate():
    """
    Examples:
        - Doctors Hate Him! See How This Cat Invented A Softer Car Using This One Weird Trick
    
    """
    
    return "{establishment} Hate {pronoun}! See How This {figure} {accomplishment} Using This One Weird Trick".format(
        establishment = sample(establishments, 1)[0],
        pronoun = sample(pronouns, 1)[0],
        figure = sample(figures, 1)[0],
        accomplishment = generate_accomplishment("past")
    )
    
def generate_reasons_why():
    """
    """
    reasons = randint(2, 100)

    return "{reasons} Reasons Why {figure}s Are {superior} Than You Think (Not Many People Know Reason #{reason_unknown})".format(
        reasons = reasons,
        figure = sample(figures, 1)[0],
        superior = sample(superiors, 1)[0],
        reason_unknown = randint(1, reasons)
        
    )

def generate_wont_believe():
    """
    You Won't Belive What This {figure} Did To {accomplishment}
    """
    
    return "You Won't Belive What This {figure} Did To {accomplishment}".format(
        figure = sample(figures, 1)[0],
        accomplishment = generate_accomplishment("present")
    )

def generate_things_didnt_know():
    """    
    Example:
    - Here are 70 Things You Didn't Know About Sweathers (Number 20 Will Shock You!)
    """ 
    
    number = randint(2, 100)
    return "Here Are {number} Things You Didn't Know About {obj}s (Number {number_shock} Will Shock You!)".format(
        number = number,
        obj = sample(objects, 1)[0],
        number_shock = randint(1, number)
    )
    
print("""
Our website needs to trick people into looking at ads!
Enter the number of clickbait headlines to generate:
""")

headlines = input(">")

while not headlines.isnumeric() or (int(headlines) < 0):
    print("Please enter a number greater than 0")
    headlines = input(">")

headlines = int(headlines)

for headline in range(0, headlines):
    headline_num = randint(1, 4)
    
    match headline_num:
        case 1:
            print(generate_establishments_hate())
        case 2:
            print(generate_reasons_why())
        case 3:
            print(generate_wont_believe())
        case 4:
            print(generate_things_didnt_know())
        case _:
            print(generate_establishments_hate())
            
    print()
