from factordb.factordb import FactorDB
from Crypto.Util.number import *
c=843044897663847841476319711639772861390329326681532977209935413827620909782846667
n=1422450808944701344261903748621562998784243662042303391362692043823716783771691667
e=65537

f = FactorDB(n)

f.get_factor_list()

f.connect()
factors = f.get_factor_list()
phi = 1
for i in factors:
	phi *= (i-1)

d = inverse(e,phi)

m = pow(c,d,n)

m = long_to_bytes(m)

print(m)