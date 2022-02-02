from Crypto.Cipher import AES
from pwn import *
key =b"1234567890123456"
print(key.encode("hex"))

def splitblocks(c):
	order = len(c)/16
	chunks, chunk_size = len(c), len(c)/order
	a = [ c[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
	raw_blocks = a
	blocks = []
	for i in range(0,order):
		blocks.append(a[i].encode("hex"))
	return blocks

flag = "tester"
plaintext = b'0000000000000000'
print(plaintext.encode("hex"))
cipher = AES.new(key, AES.MODE_CBC, key)
encrypted = cipher.encrypt(plaintext)
print(encrypted.encode("hex"))


cipher = AES.new(key, AES.MODE_CBC, key)


