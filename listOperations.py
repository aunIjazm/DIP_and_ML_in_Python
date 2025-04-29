# ----------------- without NUMPY ----------------- #
# a = [1,2,3,4,5]
# square = [i**2 for i in a if i%2==0]
# for i in a:
#     square.append(i**2)
# print(square)
# ------------------------------------------------- #


# ----------------- with NUMPY ----------------- #
import numpy as np
a = [1,2,3,4,5]
c = [[1,2,3,4,5],[6,7,8,9,10]]
b = np.array(c)
#print(b**2)
#print(type(b))
z = np.zeros((2,3))    # Defing numpy array of of all elements ZEROs of 2 ROWs and 3 COLUMNs
print(z)

p = np.array([[1,2,3,4,5],[6,7,8,9,10,],[11,12,13,14,15]])
q = p[0:2]       # Taking 2 ROWs
print(q)
r = p[:, :3]     # Taking 3 Columns
print(r)
s = p[:2, 1:3]     # Taking 3 Columns
print(s)
print(p[0,0])
print(p[2,4])
# ---------------------------------------------- #