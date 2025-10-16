# conditional statements
# ---------------------------------------------------
# Conditional Statements in Python
# ---------------------------------------------------
# Conditional statements are used to make decisions in code based on conditions.
# The main types are:
#   - if statement
#   - if-else statement
#   - if-elif-else statement
#
# Syntax and Examples:
#
# 1. if statement:
#     if condition:
#         # code block
#     Example:
# if 5 > 3:
# 	print('5 is greater than 3')
#
# 2. if-else statement:
#     if condition:
#         # code block
#     else:
#         # code block
#     Example:
# x = 10
# if x % 2 == 0:
# 	print('Even')
# else:
# 	print('Odd')
#
# 3. if-elif-else statement:
#     if condition1:
#         # code block
#     elif condition2:
#         # code block
#     else:
#         # code block
#     Example:
# num = 0
# if num > 0:
# 	print('Positive')
# elif num < 0:
# 	print('Negative')
# else:
# 	print('Zero')
# Nested if statements:
#     if condition1:
#         if condition2:
#             # code block
#         else:
#             # code block
#     else:
#         # code block
# Example:
#number = 10
# if number > 0:
#     if number % 2 == 0:
#         print('Positive Even Number')
#     else:
#         print('Positive Odd Number')
# else:
#     print('Non-positive Number')

# Example:
status =input('Enter the location')
mode=input('Enter the mode of transport')

if status == 'reached':
    if mode=='metro':
        print('reached home through metro')
    else:
        print('reached home through bus')
        
else:
    print('still on the way')




# ---------------------------------------------------
# Example usages:
# ---------------------------------------------------
# Example 1: Check if a number is positive, negative, or zero
# num = float(input('Enter a number: '))
# if num > 0:
#     print('Positive')
# elif num < 0:
#     print('Negative')
# else:
#     print('Zero')

# Example 2: Check if a year is a leap year
# year = int(input('Enter a year: '))
# if year %100==0:
#     if year%400==0:
#         print(year,"is a leap year")
#     else:
#         print(year,"is not a leap year")
# elif year % 4 == 0:
#     print(year, "is a leap year")
# else:
#     print(year,"is not a leap year")


# example 3: Check if a number is even or odd
# n=3
# if n%2==0:
#     print(n,"is even")
# else:
#     print(n,"is odd")


# Match-case statement (Python 3.10+):
#     match variable:
#         case value1:
#             # code block
#         case value2:
#             # code block
#         case _:
#             # default code block

flavour=input('Enter which flavour do you want')

match flavour:
    case 'venila':
        print('this is the general flavour of ice cream')
    case 'Strawberry':
        print('this is flavour of icecream usually liked by kids')
    case  'Custardapple':
        print('this is the natural ice cream')
    case 'chaco':
        print('This icecream is made from pure chocoletes')
    case _:
        print('the flavour is not available')







