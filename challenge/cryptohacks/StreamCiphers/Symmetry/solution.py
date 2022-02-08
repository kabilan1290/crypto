import requests
import json
from pwn import *

def splitblocks(c):
	order = len(c)/16
	chunks, chunk_size = len(c), len(c)/order
	a = [ c[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
	raw_blocks = a
	blocks = []
	for i in range(0,order):
		blocks.append(a[i].encode("hex"))
	return blocks

#http://aes.cryptohack.org/symmetry/encrypt_flag/

iv_ct = requests.get("http://aes.cryptohack.org/symmetry/encrypt_flag/")

iv_ct = json.loads(iv_ct.text)

iv_ct = iv_ct["ciphertext"]

blocks = splitblocks(iv_ct.decode("hex"))

iv = blocks[0]

#http://aes.cryptohack.org/symmetry/encrypt/+pt+iv

pt =("a"*16).encode("hex")

decrypt = requests.get("http://aes.cryptohack.org/symmetry/encrypt/"+pt+"/"+iv)

decrypt = json.loads(decrypt.text)

decrypt = decrypt["ciphertext"]
plain =("a"*16)

key = xor(plain,decrypt.decode("hex"))


p1 = xor(key,blocks[1].decode("hex"))

pt = ("a"*32).encode("hex")

decrypt = requests.get("http://aes.cryptohack.org/symmetry/encrypt/"+pt+"/"+iv)

decrypt = json.loads(decrypt.text)

decrypt = decrypt["ciphertext"]

block2 = splitblocks(decrypt.decode("hex"))

key2 = xor(plain,block2[1].decode("hex"))

p2 = xor(key2,blocks[2].decode("hex"))

print(p1+p2)