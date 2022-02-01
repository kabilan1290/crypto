from Crypto.PublicKey import RSA


# ssh-keygen -f key.pub -e -m pem > rsa.pem

key = RSA.importKey(open("rsa.pem").read())

print(key.n)