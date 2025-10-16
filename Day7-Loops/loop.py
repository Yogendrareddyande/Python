# loops in python:
# define: A loop is a programming construct that allows you to repeat a block of code multiple times until a certain condition is met. Loops are used to automate repetitive tasks and iterate over collections of data.
# types of loops:
# 1. while loop(sentinel loop)
# 2. for loop(for each loop)
# 3. nested loop

# 1. while loop:
# syntax:
# while condition:
#     # code block
# example:
# count = 0
# while count < 5:
#     print('Count:', count)
#     count += 1 

# example 2:
# i=0
# while i<5:
#     i+=1
#     print(i)
# i=5
# while i>0:
#     print(i)
    
#     i-=1


# i=1
# while i<100:
#     if i%2==0:
#         print(i)
#     i+=1
# print("done")

value=1234
count=0
while value>0:
    value//=10
    count+=1

print(count)


# Equilateral triangle pattern
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * i)


# example 4:

