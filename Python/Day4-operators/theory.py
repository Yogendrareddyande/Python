# operators:
# Arithmetic operators: +, -, *, /, %, //, **
# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
# Assignment operators: =, +=, -=, *=, /=, %=, //=, **=
# Bitwise operators: &, |, ^, ~, <<, >>
# Membership operators: in, not in
# Identity operators: is, is not

# Example 1: Arithmetic operators
a = 10
b = 3
print("Addition:", a + b)          
print("Subtraction:", a - b)       
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponentiation:", a ** b)

# Example 2: Comparison operators(relational operators)
x = 5
y = 10
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)
# Example 3: Logical operators
flag1 = True
flag2 = False
print("AND:", flag1 and flag2)   # False
print("OR:", flag1 or flag2)     # True
print("NOT:", not flag1)         # False




# Example 4: Assignment operators
c = 5
c += 2
print("c after += 2:", c)         
c *= 3
print("c after *= 3:", c)
c -= 4
print("c after -= 4:", c)
c /= 2
print("c after /= 2:", c)
c %= 3
print("c after %= 3:", c)
c //= 2
print("c after //= 2:", c)
c **= 3
print("c after **= 3:", c)

# Example 5: Bitwise operators
m = 5    # 0b0101
n = 3    # 0b0011
print( m & n)     # 1
print(m | n)      # 7
print( m ^ n)     # 6
print( ~m)        # -6
print(m << 1)     # 10
print( m >> 1)    # 2

# Example 6: Membership operators
s = "hello"
print('h' in s)          
print('z' not in s)


# Example 7: Identity operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print(list1 is list2)        
print(list1 is not list3)

p = [1, 2]
q = [1, 2]
r = p
print( p is  r)         # True
print( p is q)         # False
print( p is not q)         # True
