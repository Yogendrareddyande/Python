# nested conditional statements

# syntax:
# if condition1:
#     if condition2:
#         # code block
#     else:
#         # code block
# else:
#     # code block
# example:
number = 10
if number > 0:
    if number % 2 == 0:
        print('Positive Even Number')
    else:
        print('Positive Odd Number')
else:
    print('Non-positive Number')


status =input('Enter the location')
mode=input('Enter the mode of transport')

if status == 'reached':
    if mode=='metro':
        print('reached home through metro')
    else:
        print('reached home through bus')
        
else:
    print('still on the way')