# Brief Notes on Type Conversions and Base Conversions
# ---------------------------------------------------
#
# Examples:
#
# Type Conversion Examples
print(int('123'))      # Output: 123 (string to integer)
print(float(5))        # Output: 5.0 (integer to float)
print(str(10))         # Output: '10' (integer to string)
print(list('abc'))     # Output: ['a', 'b', 'c'] (string to list)
#
# Base Conversion Examples
print(bin(10))         # Output: '0b1010' (decimal to binary)
print(oct(10))         # Output: '0o12' (decimal to octal)
print(hex(10))         # Output: '0xa' (decimal to hexadecimal)
print(int('1010', 2))  # Output: 10 (binary string to decimal)
print(int('12', 8))    # Output: 10 (octal string to decimal)
print(int('a', 16))    # Output: 10 (hex string to decimal)
# Type Conversions:
# - Changing the data type of a value to another type.
# - Implicit conversion: Python automatically converts types (e.g., int to float).
# - Explicit conversion (Type Casting): Manual conversion using functions like int(), float(), str(), list(), etc.
#   Examples:
#     int('123')   # string to integer
#     float(5)     # integer to float
#     str(10)      # integer to string
#
# Base Conversions:
# - Converting numbers between numeral systems (binary, octal, decimal, hexadecimal).
# - Built-in functions:
#     bin(n)       # integer to binary string
#     oct(n)       # integer to octal string
#     hex(n)       # integer to hexadecimal string
#     int(s, base) # string in given base to decimal integer
#   Examples:
#     bin(10)          # returns '0b1010'
#     int('1010', 2)   # returns 10 (binary to decimal)
# ---------------------------------------------------
