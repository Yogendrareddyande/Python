# def vol(length, breadth, height): #formal parameters
#     print(length,breadth,height)
#     space=length*breadth*height
#     return space
# v=vol(5,10,3)
# print(v)


# 4. findfactor
def findfactors(n):
	"""Return a list of all factors of n."""
	return [i for i in range(1, n + 1) if n % i == 0]
print(findfactors(12))