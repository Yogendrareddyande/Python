# a=int(input('Enter first number:'))
# b=int(input('Enter second number:'))

# if a>b:
#     print(a)
# else:
#     print(a)

# a=int(input('Enter a number:'))
# if a>10:
#     if a%2==0:
#         print('a is even number')
#     else:
#         print('a is not even number')

# else:
#     print('Enter a valid number')

# a=10
# b='yogi'

# try:
#     a//b
# except (ZeroDivisionError,TypeError):
#     print('A number can not be divisible by zero')
# finally:
#     print('program completed')

a=10
b=2

try:
    res=a//b
except Exception as msg:
    print(msg)
else:
    print(res)
finally:
    print('program completed')

# Exception handling
