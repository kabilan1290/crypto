from pwn import *
#Bad Pad 2

iv_ct = "eb46aed5b08588cb899a356270626c24420aaa13f467e1ebdfca3edece4709fb3e488da22cf8a0e42f66a09763170b024f829933203d34f1b930cce298130b7425d496bd34cdea494863a93889a45e473e972753902443e38a7f77b831785120867ad44e060f344b4b95a25a0354e0565698dfd1b55b63dd6913240e7896e730757a981dee68869958d12fae662181cbecbaaa6eb477615b523445a6e79b9db0".decode("hex")
io = remote("gc1.eng.run",32755)


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

def p7dec(fake_block):
	print(fake_block)
	print(len(fake_block))
	for i in range(130,140):
		fake_block[14] = chr(i)
		temp = listToString(fake_block)
		temp = temp.encode("hex")
		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
		io.sendline(b)
		a = str(io.recvline())
		print(a)
		io.recvline()
		if "Invalid Padding" in a:
			continue
		else:
			print(a)
			c_dash = chr(i) #.encode("hex") # c'
			c_value = fake_block2[14]
			p_value = 2
			c = xor(c_dash,c_value)
			c2 = xor(p_value,c).encode("hex")
			c2 = int(c2,16)
			print("Plaintext value of P7 "+str(c2))


blocks,raw_blocks = splitblocks(iv_ct)

# I am taking the '9th block which act as an xor for 10th block' as fake_block

fake_block = list(raw_blocks[8])
fake_block2 = raw_blocks[8]
for i in range(0,1):
	#assert(i==)
	for j in range(190,200):
		temp = fake_block
		temp[15-i] = chr(j)
		temp = listToString(temp)
		temp = temp.encode("hex")
		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
		io.sendline(b)
		a = str(io.recvline())
		print(a)
		io.recvline()
		if "Invalid Padding" in a:
			continue
		else:
			if (chr(j)==fake_block2[15-i]):
				print("No")
			else:

				print(a)
				c_dash = chr(j) #.encode("hex") # c'
				c_value = fake_block2[15-i]
				print(c_value.encode("hex"))
				print #.encode("hex") # c
				p_value = i+1 # p
				c = xor(c_dash,c_value)
				c2 = xor(p_value,c).encode("hex")
				c2 = int(c2,16)
				print("Plaintext value of P8 "+str(c2))
				#[construction of the element]
				p2 = p_value+1
				final = xor(p2,c2)
				final = xor(final,c_value)
				fake_block[15-i] = final
				print("one block done")
				p7dec(fake_block)
				break





# test =['u', 'z', '\x98', '\x1d', '\xee', 'h', '\x86', '\x99', 'X', '\xd1', '/', '\xae', 'f', '!', '\x81', '\xc2']

# for i in range(1,2):


# 	for j in range(130,256):
# 		temp = test
# 		temp[15-i] = chr(j)
# 		temp = listToString(temp)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		print(a)
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			if (chr(j)==fake_block2[15]):
# 				print("No")
# 			else:

# 				print(a)
# 				c_dash = chr(j) #.encode("hex") # c'
# 				c_value = fake_block2[15-i]
# 				print(c_value.encode("hex"))
# 				print #.encode("hex") # c
# 				p_value = i+1 # p
# 				c = xor(c_dash,c_value)
# 				c2 = xor(p_value,c).encode("hex")
# 				c2 = int(c2,16)
# 				print("Plaintext value of P8 "+str(c2))
# 				#[construction of the element]
# 				p2 = p_value+1
# 				final = xor(p2,c2)
# 				print(c_value.encode("hex"))
# 				final = xor(final,c_value)
# 				fake_block[15-i] = final
# 				print("one block done")
# 				print(fake_block)






















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




