from pwn import *
#Bad Pad 2

iv_ct = "eb46aed5b08588cb899a356270626c24420aaa13f467e1ebdfca3edece4709fb3e488da22cf8a0e42f66a09763170b024f829933203d34f1b930cce298130b7425d496bd34cdea494863a93889a45e473e972753902443e38a7f77b831785120867ad44e060f344b4b95a25a0354e0565698dfd1b55b63dd6913240e7896e730757a981dee68869958d12fae662181cbecbaaa6eb477615b523445a6e79b9db0".decode("hex")
io = remote("gc1.eng.run", 31706)


def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1

def splitblocks(c):
	order = len(c)/16
	chunks, chunk_size = len(c), len(c)/order
	a = [ c[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
	raw_blocks = a
	blocks = []
	for i in range(0,order):
		blocks.append(a[i].encode("hex"))
	return blocks,a


blocks,raw_blocks = splitblocks(iv_ct)

# I am taking the '9th block which act as an xor for 10th block' as fake_block

fake_block = list(raw_blocks[8])
fake_block2 = raw_blocks[8]

# 9th block index is 8th
#---------------------------sends the oracle the data-------------------

for i in range(0,11):
	i = 15-i
	print(i)
#--------------------------------Bruteforce trying---------------------
	for j in range(0,255):
		print("hi im here")
		fake_block2 = list(fake_block2)
		fake_block2[i] = chr(j)
		fake_block2 = listToString(fake_block2)
		fake_block2 =fake_block2.encode("hex")
		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+fake_block2+blocks[9]
		#Readying up for sending
		print("hi im gere")
		fake_block = list(raw_blocks[8])
		io.sendline(b)
		a = io.recvline()
		io.recvline()
		a= str(a)
		print(a)
		if "Invalid Padding" in a:
			continue
		else:
			print("C' value :"+chr(j))
			print("C1 value : "+fake_block[i])
			print("p' value : "+ "1")
			x =xor(chr(i),fake_block[i])
			y = xor(1,x)
			print("decrypted plaintext "+str(y))
			break



































# iv = raw_blocks[8]
# fake_iv2 = list(raw_blocks[8])
# fake_iv = list(raw_blocks[8])
# for i in range(0,11):
# 	i = 4+i 
# 	intermediate = "\x13"
# 	actual = "\x11"
# 	x = xor(actual,intermediate)
# 	y = xor(fake_iv[i],x)
# 	fake_iv[i] = y

# 	print(listToString(fake_iv))
#We noticed 11 is the number of padded character

#fakeiv = listToString(fake_iv)

#fakeiv = fakeiv.encode("hex")

#b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+fakeiv+blocks[8]
#01234 56789 10 11 12 13 14 15

# for i in range(0,256):
# 	fake_iv[3] = chr(i)
# 	fakeiv = listToString(fake_iv)
# 	fakeiv = fakeiv.encode("hex")
# 	b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+fakeiv+blocks[9]
# 	io.sendline(b)
# 	a = str(io.recvline())
# 	print(a)
# 	io.recvline()
# 	if "Invalid Padding" in a:
# 		continue
# 	else:
# 		print("The value of c' "+chr(i))
# 		print("The actual value c1 "+ str(fake_iv2[4]))
# 		print("The value of p1 : /x12")
# 		intermediate = "\x12"
# 		x = xor(intermediate,chr(i))
# 		x = xor(x,fake_iv2[4])
# 		print("The expected plaintext would be "+str(x))
# 		break




