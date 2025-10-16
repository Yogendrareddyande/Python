# for loop
# syntax:
# for variable in sequence data type:
#     statement(s)
'''
# Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Example 2: Using range()
for i in range(5):
    print(i)

# Example 3: Sum of first 10 natural numbers
total = 0
for num in range(1, 11):
    total += num
print("Sum of first 10 natural numbers is:", total)

# Example 4: 
# Print prime numbers from 1 to 20
for i in range(1, 21):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i, "is a prime number")  

# Example 5: 
for i in range(1,11,1):
    print(i)
for i in range(10,0,-1):
    print(i)
for i in range(1,11,2):
    print(i)



# Example 6:
# Print multiplication table of a given number
num=int(input("Enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
'''

# Example 7:nested for loop
for i in range(1,4):
    for j in range(1,4):
        print(i,j)

# Example 8:
# Print pattern
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()



# Example 9:
# Print equalateral traingle pattern
# Equilateral triangle pattern
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * i)

# Example 10:
# Print reverse equilateral triangle pattern
rows = 5
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '* ' * i)

# Example 11:
# Print diamond pattern
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * i)

for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '* ' * i)