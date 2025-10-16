import random

points = 0
rounds = 5

print("Welcome to the Number Match Game!")
print("You start with 0 points. Guess the correct number (between 1 and 5) to earn 10 points.\n")

for i in range(1, rounds + 1):
    user_input = int(input(f"Round {i}: Enter a number between 1 and 5: "))
    random_number = random.randint(1, 5)
    
    if user_input == random_number:
        points += 10
        print(f"Correct! The number was {random_number}. You earn 10 points.\n")
    else:
        print(f"Wrong! The number was {random_number}. You earn 0 points.\n")

print(f"Game Over! Your final score: {points}points")