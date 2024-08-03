"""
Collatz Sequence
"""

print("Collatz Sequence, or, the 3n + 1 Problem")
print("""\n
The Collatz sequence is a sequence of numbers produce from a starting number n, following theee rules:

1. If n is even the next number is n / 2.
2. If n is odd, the next number is (n * 3) + 1.
3. If n is 1, stop. 
""")

def start_sequence(num: int):
    while num != 1:
        print(num, end='')
        
        if num % 2 == 0:
            num = round(num / 2)
        else:
            num = (num * 3) + 1
        
        print(", ", end='')
    
    print(num, end='')

def init_sequence():
    print("Enter a starting number (greater than 0) or QUIT:")
    starting_num = input(">")
    
    if starting_num.lower() == "quit":
        return 
    
    while not starting_num.isnumeric() or int(starting_num) < 0:
        print("Please enter a starting number (greater than 0) or QUIT:")
        starting_num = input(">")
        
        if starting_num.lower() == "quit":
            return
    
    starting_num = int(starting_num)
    start_sequence(starting_num)
        
if __name__ == '__main__':
    init_sequence()
