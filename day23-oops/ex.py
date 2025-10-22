# What is OOPS?
# OOPS stands for Object-Oriented Programming System.
# It is a programming paradigm (a way to structure programs) that organizes code using objects and classes instead of plain functions.

# Everything in OOPS revolves around Classes and Objects.

# Class Is	a blueprint or template for creating objects.
# and a group of variables and methods is a class.

# Object	An instance (real example) of a class.
# Method	A function defined inside a class.
# Attribute	A variable that belongs to a class or an object.

# class
# object
# Encapsulation (protection of code)
# inheritance (Types)
# abstraction (access specifiers )
# polymorphisum (method overloading and overriding in java)

'''
class classname:
    def __init__(self,parameters):
              parameters variables declaration

    def add (self,a,b):
         a+b 


a=classname()
a.add(10,20)
b=classname()

'''
# class has two types 
# class variable and instance variable
class Example:
    # owner='yogi' class define  variable  # print(Example.owner)
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Displayname(self):
        print(self.name)
    
    def Displayage(self):
        print(self.age)

ins1=Example('Achiverit',11)

ins1.Displayname()
ins2=Example('9globes',3)
ins2.Displayage()


