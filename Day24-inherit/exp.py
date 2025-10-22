# What is Inheritance in OOPs?

# Inheritance is one of the core concepts of Object-Oriented Programming (OOP).
# It allows one class (called the child or derived class) to acquire properties and behaviors (methods and attributes) from another class (called the parent or base class).

# It helps to reuse existing code and extend functionality without rewriting it.

# types
# 1.Single Inheritance
# One child inherits from one parent
# A → B

# 2.Multiple Inheritance
# A child inherits from more than one parent
# A, B → C

# 3.Multilevel Inheritance
# A child inherits from a parent, and another child inherits from that child
# A → B → C

# 4.Hierarchical Inheritance
# Multiple children inherit from the same parent
# A → B, C

# 5.Hybrid Inheritance
# A combination of two or more types above
# Combination of multiple


# 1.Basic inheritance(single)
class parent:
    def __init__(self):
        pass

    def display(self):
        print('This is parent Class')

class child(parent):
    def __init__(self):
        pass
    def show (self):
        print('This is a child class')

c=child()
c.display()
c.show()


# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class inherits Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Object of child class
d = Dog()
d.speak()  # Inherited method
d.bark()



# 2.multiple inheritance
class Daddy:
    def skill(self):
        print('He is a good business man')

class mommy:
    def talent(self):
        print('She is a singer')

class son(Daddy,mommy):
    def own (self):
        print('He is agood dancer')

s=son()
s.skill()
s.talent()
s.own()


# 3.multilevel inheritance

class Grandfather:
    def __init__(self):
        pass
    def head(self):
        print('He is the head of the family')

class Father(Grandfather):
    def __init__(self):
        pass

    def earning(self):
        print('He is the one who as earns')

class Grandson(Father):
    def __init__(self):
        pass

    def study(self):
        print('He is studying')


g=Grandson()
g.head()
g.earning()
g.study()


# 4.hirarchical

class Dad:
    def __init__(self):
        pass
    def bussiness(self):
        print('He as a bussiness')

class firstson(Dad):
    def __init__(self):
       pass
    def Account(self):
        print('He is an account')

class secondson(Dad):
    def __init__(self):
        pass
    def Digi(self):
        print('He is a also digital marketing agent')

f=firstson()
f.bussiness()
f.Account()

s=secondson()
s.Digi()
s.bussiness()