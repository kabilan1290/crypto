#https://n1be.kr/entry/CryptoHack-Extended-GCD

def computeGCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x
# return (u, v) such that au + bv = gcd(a, b)
def extended_euclidean(a, b): # a > b
    if a < b:
        return 0, 0
    else:
        if a % b == computeGCD(a, b):
            return 1, 0 - int(a / b)
        else:
            u, v = extended_euclidean(b, a % b)
            return v, u - v * int(a / b)

p = 26513
q = 32321

print(extended_euclidean(q,p))

#a * u + b * v = gcd(a,b)

# (26513*10245)+(32321*-8404) = 1