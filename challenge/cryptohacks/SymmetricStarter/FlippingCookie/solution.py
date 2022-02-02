import requests
from pwn import *
#import json
#x = requests.get("http://aes.cryptohack.org/flipping_cookie/get_cookie")

#y = json.loads(x.text)
#print(y["cookie"])
#b6322df0b853de520f4fb04a42e76683c8d3f26a232da6263be70f1168e502b7ea820c1835e1a88624876fe4f6918cc3

cookie = "b6322df0b853de520f4fb04a42e76683c8d3f26a232da6263be70f1168e502b7ea820c1835e1a88624876fe4f6918cc3"

def splitblocks(c):
	order = len(c)/16
	chunks, chunk_size = len(c), len(c)/order
	a = [ c[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
	raw_blocks = a
	blocks = []
	for i in range(0,order):
		blocks.append(a[i].encode("hex"))
	return blocks


blocks = splitblocks(cookie.decode("hex"))

IV = blocks[0]

CT = blocks[1]

# what we have admin=False
# what we need admin=True;
#print(len("admin=")) // 6 characters

#print(len("admin=True;")) // 11 characters
p1 = "admin=False"
intermitiate_value = ""
for i in range(0,11):
	iv = IV.decode("hex")
	ct = p1
	intermitiate_value += xor(iv[i],ct[i])

needed_value = "admin=True;"
new_iv = ""
for i in range(0,11):
	new_iv += xor(intermitiate_value[i],needed_value[i])

print(new_iv.encode("hex")+"4a42e76683")
print(blocks[1]+blocks[2])