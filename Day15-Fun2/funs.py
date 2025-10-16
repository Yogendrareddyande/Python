# def fun(a=1,b=2.5,c=[3,4,5]):
#     print(a,b,c)

# fun()

# def fun(a,b,c,d,e,/):
#     print(a,b,c,d,e)

# fun(10,20,30,40,50)

def fun(a,b,*,c,d,e):
    print(a,b,c,d,e)
fun(10,20,c=30,d=40,e=50)






