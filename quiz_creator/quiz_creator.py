"""
Quiz Creator
"""

from random import randint

questions = []

print("How many questions do you want to create?")
num_questions = input(">")

# Ensure num_questions is valid
while not num_questions.isnumeric() and num_questions <= 0:
    print("Please enter a number greater than 0")
    num_questions = input(">")

num_questions = int(num_questions)

# Get all questions and answers
for question in range(0, num_questions):
    print("Enter question: ")
    current_question = input(">")
    print("Enter answer: ")
    current_answer = input(">")

    questions.append({
        "quest": current_question,
        "ans": current_answer
    })


# Ask questions randomly
print("Quiz Begins...")

correct = 0

while len(questions) != 0:
    index = randint(0, len(questions)-1)
    current_question = questions[index]

    print("Question: ", current_question["quest"])
    user_answer = input(">")

    if user_answer == current_question["ans"]:
        print("Correct!")
        correct += 1
    else:
        print("Incorrect")
        print("Answer: ", current_question["ans"])
    
    questions.pop(index)

# Display amount correct
print("{}/{}".format(correct, num_questions))
