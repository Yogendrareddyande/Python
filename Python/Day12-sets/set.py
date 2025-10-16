# sets:
# set is an group of unique elements
# it canonot have duplicate elements
# unordered collection of unique elements
# defined by curly braces {}
#it accept heterogeneous elements
'''
s1={}
print(type(s1))  # this is dictionary not set



s={1, 2, 3, 4, 5, 1, 2, 3}
print(s)

for i in s:
    print(i)


s2=set([1, 2, 3, 4, 5, 1, 2, 3])
print(s2)

s3=set('python')
print(s3)   

s4={1,2.5,'python',12+11j}
print(s4)



s={10,20,30,40,50}
s.add(60)
print(s)

s.pop()
print(s)

s.remove(20)
print(s)

s.discard(30)
print(s)

s.clear()
print(s)

'''
'''
# sets in mathematics
'''
s1={1,2,3,4,5,6,7,8,9,10}
a={2,4,6,8,10}
b={1,3,5,7,9}
c={1,2,3,4,5,6,7,8,9,10}
print(s1.issubset(c))
print(a.issubset(s1))
print(b.issubset(s1))
print(c.issubset(s1))

print(s1.issuperset(a))


# sets methods
'''
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))


# symbols
print(A|B)
print(A&B)
print(A-B)
print(A^B)



# add()
A.add(6)
print(A)

A.update((7,8,9))
print(A)

C=A.copy()
print(C)

A.clear()
print(A)
'''

# set comprehension
'''
s={x*x for x in range(1,6)}
print(s)

s1={x for x in 'python programming' if x not in 'aeiou'}
print(s1)
'''



