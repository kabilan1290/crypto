from Crypto.Cipher import DES3
import os
from pwn import xor

IV = os.urandom(8)
print(IV.encode("hex"))

KEY = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"#key = bytes.fromhex(key)
#plaintext = b'cryptoio'
plaintext = "8a51ce5c3d98f54d".decode("hex")
print("Plaintext "+plaintext.encode("hex"))

#plaintext = xor(plaintext, IV)
cipher = DES3.new(KEY, DES3.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)

print(ciphertext)
