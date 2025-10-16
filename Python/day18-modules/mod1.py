# print(__name__)

a=10
b=20
def add(a, b):
    print("Sum is:", a+b)


def sub(a, b):
    print("Subtraction is:", a-b)

if __name__=="__main__":
    add(a,b)
    sub(a,b)