# import math 

# print(math.sqrt(144))
# print(math.pi)
# print(dir(math))
# print(math.e)  

# import math as m
# print(m.sqrt(144))
# print(m.pi) 

# from math import pi, sqrt
# print(sqrt(144))

import random
# print(random.random())
# print(random.uniform(10,20))
# print(random.randint(1,6))
# print(random.randrange(10,100,5))

# otp=random.randint(1000,9999)
# print("Your OTP is:", otp)

# list1=['yogi', 'ram', 'sham', 'mohan', 'sohan']
# print(random.choice(list1))
# print(random.choices(list1, k=3))
# random.shuffle(list1)
# l1=list(range(1,31))

# print(l1)

# print(random.choice(l1))
# print(random.choices(l1, k=3))


# create a game using a random module
l1=list(range(1,11))
print("Welcome to the number guessing game")
print("You have 5 chances to guess the correct number between 1 to 10")
n=random.choice(l1)
chances=5
while chances>0:
    g=int(input("Enter your guess: "))
    if g==n:
        print("Congratulations! You guessed the correct number")
        break
    elif g<n:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    chances-=1
    print("You have", chances, "chances left")
    