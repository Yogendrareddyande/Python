# Tuples:
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.
# Tuples are similar to lists, but the key difference is that tuples cannot be changed (they are immutable) while lists can be modified (they are mutable).
# Tuples are defined by parentheses ().
# Tuples can contain heterogeneous elements.
# Tuples are indexed, allowing access to individual elements.
# Tuples allow duplicate elements.
t=(10,20,30,40,50,10,20,30)
print(t)
print(type(t))
print(len(t))
print(t[0])
print(t[3])
print(t[-1])
print(t[-4])
print(t[2:5])
print(t[1:])
print(t[:4])
print(t[:])
# t[3]=100  # This will raise an error because tuples are immutable
print(t*3)
print(t+('python','java'))
print(t)
for i in t:
    print(i)
t1=(1,2,3)
# t1.append(40)  # This will raise an error because tuples do not have an append method
# t1.insert(1,20)  # This will raise an error because tuples do not have an insert method

# t1.remove(3)  # This will raise an error because tuples do not have a remove method
# t1.pop()  # This will raise an error because tuples do not have a pop method
# t1.pop(1)  # This will raise an error because tuples do not have a pop method
# t1.clear()  # This will raise an error because tuples do not have a clear method
t2=(1,2,3,4,5)
# t2.extend([6,7,8])  # This will raise an error because tuples do not have an extend method
# t2.sort()  # This will raise an error because tuples do not have a sort method
# t2.reverse()  # This will raise an error because tuples do not have a reverse method
t3=('python','java','c','c++')
t3_sorted=tuple(sorted(t3))
print(t3_sorted)