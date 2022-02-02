import requests
import json
from pwn import *
#http://aes.cryptohack.org/lazy_cbc/

#Only accepts hex input

a = ("a"*16).encode("hex")

#encrypt = requests.get("http://aes.cryptohack.org/lazy_cbc/encrypt/"+a)

#x = json.loads(encrypt.text)

#print(x["ciphertext"])
#e300055fd0eb79500d968e9d83734d57

c1 ="e300055fd0eb79500d968e9d83734d57"
c3 = "e300055fd0eb79500d968e9d83734d57"
c2 = "0"*32

c = c1+c2+c3

#decrypt = requests.get("http://aes.cryptohack.org/lazy_cbc/receive/"+c)

#x = json.loads(decrypt.text)

#print(x["error"])

plaintext = "61616161616161616161616161616161ed993cc06a0d3bc7047e16a9bf12313c084222bd660df17baa3a8a9b11ca59f1".decode("hex")

def splitblocks(c):
	order = len(c)/16
	chunks, chunk_size = len(c), len(c)/order
	a = [ c[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
	raw_blocks = a
	blocks = []
	for i in range(0,order):
		blocks.append(a[i].encode("hex"))
	return blocks

blocks = splitblocks(plaintext)

p1 = blocks[0].decode("hex")

p3 = blocks[2].decode("hex")

key = ""

for i in range(0,16):
	key += xor(p1[i],p3[i])

key =  key.encode("hex")

flag = requests.get("http://aes.cryptohack.org/lazy_cbc/get_flag/"+key)

x = json.loads(flag.text)
y = x["plaintext"]

print(y.decode("hex"))
