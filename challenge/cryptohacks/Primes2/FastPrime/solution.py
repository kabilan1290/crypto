from Crypto.PublicKey import RSA
from sympy.ntheory.primetest import is_square
from Crypto.Util.number import long_to_bytes,inverse
import sympy
key = RSA.importKey(open("key.pem").read())

n = key.n
e = key.e

def fermat(n):
    a = int(sympy.sqrt(n)) # Fermat's Algorithm
    b = (a*a) - n
    while not is_square(b):
        a += 1
        b = (a*a) - n
    else:
        p = int(a - (sympy.sqrt(b)))
        q = n//p
        if p * q == n:
            return p,q
        else:
            return "No Luck"

print(key.e)