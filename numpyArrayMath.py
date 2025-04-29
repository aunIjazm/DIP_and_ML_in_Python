import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64())
y = np.array([[5,6],[7,8]], dtype=np.float64())

print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))

print(x+y)
print(np.add(x,y))
print(x*y)
print(np.multiply(x,y))

print(x.T)  # Transpose


# Broadcasting of Array
a = np.array([[1,2,3],[4,5,6],[7,8,9], [4,7,9]])
b = np.array([2,0,2])
c = a+b
print(c)