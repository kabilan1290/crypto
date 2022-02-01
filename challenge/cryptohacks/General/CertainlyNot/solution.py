from asn1crypto.x509 import Certificate

with open("RSA.der", "rb") as f:
    cert = Certificate.load(f.read())

n = cert.public_key.native["public_key"]["modulus"]
e = cert.public_key.native["public_key"]["public_exponent"]
print(n)
print(e)