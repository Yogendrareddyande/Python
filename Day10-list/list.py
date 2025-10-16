# list:
# - ordered
# - mutable
# - allows duplicate elements
# - defined by square brackets []
# - accepts heterogeneous elements
# - indexed
l=[10,20,30,40,50,10,20,30]
print(l)

print(type(l))
print(len(l))
print(l[0])
print(l[3])
print(l[-1])
print(l[-4])
print(l[2:5])
print(l[1:])
print(l[:4])
print(l[:])

l[3]=100
print(l)
print(l*3)
print(l+['python','java'])
print(l)
for i in l:
    print(i)
L1=[1,2,3]
L1.append(40)
print(L1)
L1.insert(1,20)
print(L1)
L1.remove(3)
print(L1)

L1.pop()
print(L1)

L1.pop(1)
print(L1)
L1.clear()
print(L1)

L2=[1,2,3,4,5]
L2.extend([6,7,8])
print(L2)

L2.sort()
print(L2)
L2.reverse()
print(L2)

L3=['python','java','c','c++']
L3.sort()
print(L3)

L3.reverse()
print(L3)

L4=['python','java','c','c++','python','java']
print(L4.count('python'))
print(L4.index('c++'))

L4.remove('python')
print(L4)

L4.remove('python')
print(L4)

L4.append('python')
print(L4)


L4.insert(2,'python')
print(L4)
L4.insert(4,'python')
print(L4)
L4.pop(3)
print(L4)
L4.pop()
print(L4)
L4.clear()
print(L4)
L4.extend(['python','java','c','c++','python','java'])
print(L4)

