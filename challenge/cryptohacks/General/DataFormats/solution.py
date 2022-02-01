from Crypto.PublicKey import RSA

key = RSA.importKey(open("public.pem").read())

print(key.d)