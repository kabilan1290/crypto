from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from pwn import *


KEY = b'1234567890123456'
FLAG = b"crytpo{some_flipping_is_needed}"
cookie = b'bdmin=1;admin=2;admin3'
iv = "35ac09fc3a43f9aab95e4950f8c9ce73".decode("hex")
padded = pad(cookie, 16)
cipher = AES.new(KEY, AES.MODE_CBC, iv)
encrypted = cipher.encrypt(padded)
ciphertext = iv.encode("hex") + encrypted.encode("hex")

print("This is cipher "+ciphertext)
def splitblocks(c):
	order = len(c)/16
	chunks, chunk_size = len(c), len(c)/order
	a = [ c[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
	raw_blocks = a
	blocks = []
	for i in range(0,order):
		blocks.append(a[i].encode("hex"))
	return blocks
blocks = splitblocks(ciphertext.decode("hex"))

def decryption(iv,KEY,cookie):
	cipher = AES.new(KEY, AES.MODE_CBC, iv)
	decrypted = cipher.decrypt(cookie)
	unpadded = unpad(decrypted, 16)
	print(unpadded)

#decryption(iv,KEY,ciphertext.decode("hex"))

a = "b"
b = "35".decode("hex")

c  = xor(a,b)
d = xor(c,"a")
print(d.encode("hex"))
iv2 ="36ac09fc3a43f9aab95e4950f8c9ce73".decode("hex")
ciphertext2 = "c314859741fa0ad32cf6c4586257cda740925ec58134ee186d026d939b8ad832"
decryption(iv2,KEY,ciphertext2.decode("hex"))
