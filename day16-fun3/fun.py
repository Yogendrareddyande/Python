# def fun(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
# fun(1,2,3,4,5,6,7,8,9,10)

# def fun1(**kwargs):
#     for i in kwargs.items():
#         print(i[0], ":", i[1])

# fun1(name='yogi', age=21, city="pune", country="India")

# def fun(*args, **kwargs):
#     print(args)
#     print(kwargs)

# fun(1,2,3,4,5,a=6,b=7,c=8,d=9,e=10)

# print(print.__doc__)

# show=print
# show("Hello World")

# take=input
# t=take("Enter your number: ")
# print(t)

# def fun(a,b,c,/,d,e):
#     print(a,b,c,d,e)
# fun(10,20,30,d=40,e=50)


# *aargs and **kargs
def fun(*args, **kwargs):
    print(args)
    print(kwargs)
fun(1,2,3,4,5,a=6,b=7,c=8,d=9,e=10)

# another example
def fun1(*args, **kwargs):
    sum = 0
    for i in args:
        sum += i
    print("Sum of args:", sum)
    for k, v in kwargs.items():
        print(k, ":", v)
fun1(1,2,3,4,5,name="yogi", age=21, city="pune")