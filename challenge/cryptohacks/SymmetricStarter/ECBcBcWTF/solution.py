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


c = "2f087d660c53a9f881d239c084046e55769da319740a55362b462cf4fb1f41ddbdfbea611a58c3fd91027a7c3ff8c77c".decode("hex")

blocks = splitblocks(c)

IV = blocks[0]
c1 = blocks[1]
c2 = blocks[2]

# D(c1) ^ IV = p1
#Sending C1 in the decryption oracle
D_c1 = "4c7a0416783cd2cbe2b066f5f1670560".decode("hex")
plaintext=""
for i in range(0,16):
	iv = IV.decode("hex")
	plaintext += xor(D_c1[i],iv[i])

# D(c2) ^ c1 = p2
#Sending C2 in the decryption oracle
D_c2 = "29a9d529456e0a071c190dd5da3e60a0".decode("hex")
p2=""
for i in range(0,16):
	iv = c1.decode("hex")
	plaintext += xor(iv[i],D_c2[i])
print(plaintext)