# strings
# define
# A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). Strings are used to represent text data in Python.
# types of strings
# 1. single line string
# 2. multi line string
# creating strings
s1 = 'Hello'
s2 = "World"
s3 = '''This is a'''
s4 = """multi-line string"""

print(s1)
print(s2)
print(s3)
print(s4)
# string operations
# concatenation
s5 = s1 + ' ' + s2
print(s5)
# repetition
s6 = s1 * 3
print(s6)
# indexing
print(s1[0])
print(s1[-1])
# slicing
print(s1[1:4])
print(s1[:3])
print(s1[2:])
print(s1[-4:-1])
# string methods
print(s1.lower())
print(s2.upper())
print(s5.split())
print(s5.replace('World', 'python'))
print(s1.startswith('H'))
print(s2.endswith('d'))
print(s1.find('e'))
print(len(s5))
print(s5.count('l'))
print(s5.isalpha())
print(s5.isalnum())
print(s5.isspace())
print(s5.title())
print(s5.capitalize())
print(s5.center(20, '-'))
print(s5.ljust(20, '-'))
print(s5.rjust(20, '-'))
print(s5.strip('-'))
print(s5.swapcase())
print(s5.partition(' '))
print(s5.rpartition(' '))
print(s5.zfill(20))
print(s5.encode())
print(s5.expandtabs(10))
print(s5.format())
print(s5.index('W'))


# escape sequences
print('I\'m learning Python')
print("He said, \"Hello!\"")
print("Line1\nLine2")
print("Column1\tColumn2")
print("Backslash: \\")
