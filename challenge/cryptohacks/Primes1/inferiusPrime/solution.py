from gmpy2 import *
from Crypto.Util.number import *
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
n = 742449129124467073921545687640895127535705902454369756401331

#Using factordb to factorize n

p = 752708788837165590355094155871

q = n // p

phi =(p-1)*(q-1)

d = inverse(e,phi)

m = pow(ct,d,n)

print(long_to_bytes(m))

