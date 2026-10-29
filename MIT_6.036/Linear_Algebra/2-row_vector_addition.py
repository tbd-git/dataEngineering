# Addition of two lists 
a=[1,5,-3,2] 
b=[8,2,4,7]
print("zip: ",zip(a,b),list(zip(a,b)))
c=[x+y for x, y in zip(a, b)]
print("Zipped addition C: ",c)
# What does zip do?
# The `zip` function in Python takes two or more iterables (like lists) 
# and returns an iterator of tuples, 
# where the i-th tuple contains the i-th element from each of the input iterables. 
# In the context of your code, `zip(a, b)` pairs up the elements of lists `a` and `b` together, 
# so that you can easily iterate over them in parallel.
c=[]
for i in range(len(a)):
    c.append(a[i] + b[i])
print("Loop addition C: ",c)