from Crypto.Util.number import *
from gmpy2 import *

n = 95341235345618011251857577682324351171197688101180707030749869409235726634345899397258784261937590128088284421816891826202978052640992678267974129629670862991769812330793126662251062120518795878693122854189330426777286315442926939843468730196970939951374889986320771714519309125434348512571864406646232154103
e = 3
ct = 63476139027102349822147098087901756023488558030079225358836870725611623045683759473454129221778690683914555720975250395929721681009556415292257804239149809875424000027362678341633901036035522299395660255954384685936351041718040558055860508481512479599089561391846007771856837130233678763953257086620228436828

def is_cube(n):
    cube_root = n**(1./3.)
    if round(cube_root) ** 3 == n:
        print(True)
    else:
        print(False)

for i in range(0,100):
	padding_length = 100-i
	new_ct = ct * pow(inverse(256, n) ** padding_length, e, n)
	new_ct %= n
	for i in range(256):
		potential_pt, is_cube = iroot(new_ct + (n * i), e)
		if is_cube:
			print(i, long_to_bytes(potential_pt))