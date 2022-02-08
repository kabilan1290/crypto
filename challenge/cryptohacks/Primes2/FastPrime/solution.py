from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long,long_to_bytes,inverse
from Crypto.Cipher import PKCS1_OAEP

key = RSA.importKey(open("key.pem").read())

n = key.n
e = key.e

p = 77342270837753916396402614215980760127245056504361515489809293852222206596161
q = n // p

phi=(p-1)*(q-1)

c = "249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28".decode("hex")

#c = bytes_to_long(c)

d =inverse(e,phi)
key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)

m = cipher.decrypt(c)
print(m)