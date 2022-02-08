from gmpy import *
v = [4, 6, 2, 5]

v_2 = [i*i for i in v]

v_2 = sum(v_2)

print(root(v_2,2)[0])