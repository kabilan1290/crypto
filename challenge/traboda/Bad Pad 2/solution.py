from pwn import *
#Bad Pad 2

iv_ct = "eb46aed5b08588cb899a356270626c24420aaa13f467e1ebdfca3edece4709fb3e488da22cf8a0e42f66a09763170b024f829933203d34f1b930cce298130b7425d496bd34cdea494863a93889a45e473e972753902443e38a7f77b831785120867ad44e060f344b4b95a25a0354e0565698dfd1b55b63dd6913240e7896e730757a981dee68869958d12fae662181cbecbaaa6eb477615b523445a6e79b9db0".decode("hex")
#io = remote("gc1.eng.run",30185)


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

print("[+]Success Padding Oracle Attack")
print("[+]Recovered 5 bytes : ~lse}")
blocks,raw = splitblocks(iv_ct)
iv = raw[8]
print("[+]Lenth of original bytes "+str(len(iv)))
iv_orginal = iv[:5]
p_value = "~lse}"
fake=""
for i in range(0,5):
	fake+=xor(iv_orginal[i],p_value[i])

needed ="Admin"
print("[+]Required 5 bytes : Admin")
fake2 =""
for i in range(0,5):
	fake2+=xor(fake[i],needed[i])

fake_iv = (fake2+iv[5:]).encode("hex")

print("[+]Crafted IV :" +fake_iv)

b=fake_iv+blocks[9]
print(b)
# def p17dec(fake_block,p1,fake_block2):
# 	for i in range(130,140):
# 		fake_block[14] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[14]
# 			p_value = 2
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p2 = int(c2,16)
# 			print("Plaintext value of P15 "+str(p2))
# 			p_value = 3
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			p16dec(fake_block,p1,p2,fake_block2)
# 			break


# def p16dec(fake_block,p1,p2,fake_block2):
# 	for i in range(0,256):
# 		fake_block[13] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[13]
# 			p_value = 3
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p3 = int(c2,16)
# 			print("Plaintext value of P14 "+str(p3))
# 			p_value = 4
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			p15dec(fake_block,p1,p2,p3,fake_block2)
# 			break

# def p15dec(fake_block,p1,p2,p3,fake_block2):
# 	for i in range(0,256):
# 		fake_block[12] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())

# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[12]
# 			p_value = 4
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p4 = int(c2,16)
# 			print("Plaintext value of P13 "+str(p4))
# 			p_value = 5
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			c4 = fake_block2[12]

# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			a = xor(p4,c4)
# 			b= xor(p_value,a)
# 			fake_block[12] = b
# 			p14dec(fake_block,p1,p2,p3,p4,fake_block2)
# 			break

# def p14dec(fake_block,p1,p2,p3,p4,fake_block2):
# 	for i in range(0,256):
# 		fake_block[11] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[11]
# 			p_value = 5
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p5 = int(c2,16)
# 			print("Plaintext value of P12 "+str(p5))
# 			p_value = 6
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			c4 = fake_block2[12]
# 			c5 = fake_block2[11]
# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			a = xor(p4,c4)
# 			b= xor(p_value,a)
# 			fake_block[12] = b
# 			a = xor(p5,c5)
# 			b= xor(p_value,a)
# 			fake_block[11] = b			
# 			p13dec(fake_block,p1,p2,p3,p4,p5,fake_block2)
# 			break

# def p13dec(fake_block,p1,p2,p3,p4,p5,fake_block2):
# 	for i in range(0,256):
# 		fake_block[10] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[10]
# 			p_value = 6
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p6 = int(c2,16)
# 			print("Plaintext value of P11 "+str(p6))
# 			p_value = 7
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			c4 = fake_block2[12]
# 			c5 = fake_block2[11]
# 			c6 = fake_block2[10]

# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			a = xor(p4,c4)
# 			b= xor(p_value,a)
# 			fake_block[12] = b
# 			a = xor(p5,c5)
# 			b= xor(p_value,a)
# 			fake_block[11] = b	
# 			a = xor(p6,c6)
# 			b= xor(p_value,a)
# 			fake_block[10] = b		
# 			p12dec(fake_block,p1,p2,p3,p4,p5,p6,fake_block2)
# 			break

# def p12dec(fake_block,p1,p2,p3,p4,p5,p6,fake_block2):
# 	for i in range(0,256):
# 		fake_block[9] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[9]
# 			p_value = 7
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p7 = int(c2,16)
# 			print("Plaintext value of P10 "+str(p7))
# 			p_value = 8
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			c4 = fake_block2[12]
# 			c5 = fake_block2[11]
# 			c6 = fake_block2[10]
# 			c7 = fake_block2[9]

# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			a = xor(p4,c4)
# 			b= xor(p_value,a)
# 			fake_block[12] = b
# 			a = xor(p5,c5)
# 			b= xor(p_value,a)
# 			fake_block[11] = b	
# 			a = xor(p6,c6)
# 			b= xor(p_value,a)
# 			fake_block[10] = b
# 			a = xor(p7,c7)
# 			b= xor(p_value,a)
# 			fake_block[9] = b		
# 			p11dec(fake_block,p1,p2,p3,p4,p5,p6,p7,fake_block2)
# 			break

# def p11dec(fake_block,p1,p2,p3,p4,p5,p6,p7,fake_block2):
# 	for i in range(0,256):
# 		fake_block[8] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[8]
# 			p_value = 8
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p8 = int(c2,16)
# 			print("Plaintext value of p9 "+str(p8))
# 			p_value = 9
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			c4 = fake_block2[12]
# 			c5 = fake_block2[11]
# 			c6 = fake_block2[10]
# 			c7 = fake_block2[9]
# 			c8 = fake_block2[8]

# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			a = xor(p4,c4)
# 			b= xor(p_value,a)
# 			fake_block[12] = b
# 			a = xor(p5,c5)
# 			b= xor(p_value,a)
# 			fake_block[11] = b	
# 			a = xor(p6,c6)
# 			b= xor(p_value,a)
# 			fake_block[10] = b
# 			a = xor(p7,c7)
# 			b= xor(p_value,a)
# 			fake_block[9] = b
# 			a = xor(p8,c8)
# 			b= xor(p_value,a)
# 			fake_block[8] = b	
# 			p10dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,fake_block2)
# 			break

# def p10dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,fake_block2):
# 	for i in range(0,256):
# 		fake_block[7] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[7]
# 			p_value = 9
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p9 = int(c2,16)
# 			print("Plaintext value of p8 "+str(p9))
# 			p_value = 10
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			c4 = fake_block2[12]
# 			c5 = fake_block2[11]
# 			c6 = fake_block2[10]
# 			c7 = fake_block2[9]
# 			c8 = fake_block2[8]
# 			c9 = fake_block2[7]
# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			a = xor(p4,c4)
# 			b= xor(p_value,a)
# 			fake_block[12] = b
# 			a = xor(p5,c5)
# 			b= xor(p_value,a)
# 			fake_block[11] = b	
# 			a = xor(p6,c6)
# 			b= xor(p_value,a)
# 			fake_block[10] = b
# 			a = xor(p7,c7)
# 			b= xor(p_value,a)
# 			fake_block[9] = b
# 			a = xor(p8,c8)
# 			b= xor(p_value,a)
# 			fake_block[8] = b
# 			a = xor(p9,c9)
# 			b= xor(p_value,a)
# 			fake_block[7] = b		
# 			p9dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,fake_block2)
# 			break

# def p9dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,fake_block2):
# 	for i in range(0,256):
# 		fake_block[6] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[6]
# 			p_value = 10
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p10 = int(c2,16)
# 			print("Plaintext value of p7 "+str(p10))
# 			p_value = 11
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			c4 = fake_block2[12]
# 			c5 = fake_block2[11]
# 			c6 = fake_block2[10]
# 			c7 = fake_block2[9]
# 			c8 = fake_block2[8]
# 			c9 = fake_block2[7]
# 			c10 = fake_block2[6]

# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			a = xor(p4,c4)
# 			b= xor(p_value,a)
# 			fake_block[12] = b
# 			a = xor(p5,c5)
# 			b= xor(p_value,a)
# 			fake_block[11] = b	
# 			a = xor(p6,c6)
# 			b= xor(p_value,a)
# 			fake_block[10] = b
# 			a = xor(p7,c7)
# 			b= xor(p_value,a)
# 			fake_block[9] = b
# 			a = xor(p8,c8)
# 			b= xor(p_value,a)
# 			fake_block[8] = b
# 			a = xor(p9,c9)
# 			b= xor(p_value,a)
# 			fake_block[7] = b
# 			a = xor(p10,c10)
# 			b= xor(p_value,a)
# 			fake_block[6] = b		
# 			p8dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,fake_block2)
# 			break

# def p8dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,fake_block2):
# 	for i in range(0,256):
# 		fake_block[5] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[5]
# 			p_value = 11
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p11 = int(c2,16)
# 			print("Plaintext value of p6 "+str(p11))
# 			p_value = 12
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			c4 = fake_block2[12]
# 			c5 = fake_block2[11]
# 			c6 = fake_block2[10]
# 			c7 = fake_block2[9]
# 			c8 = fake_block2[8]
# 			c9 = fake_block2[7]
# 			c10 = fake_block2[6]
# 			c11 = fake_block2[5]
# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			a = xor(p4,c4)
# 			b= xor(p_value,a)
# 			fake_block[12] = b
# 			a = xor(p5,c5)
# 			b= xor(p_value,a)
# 			fake_block[11] = b	
# 			a = xor(p6,c6)
# 			b= xor(p_value,a)
# 			fake_block[10] = b
# 			a = xor(p7,c7)
# 			b= xor(p_value,a)
# 			fake_block[9] = b
# 			a = xor(p8,c8)
# 			b= xor(p_value,a)
# 			fake_block[8] = b
# 			a = xor(p9,c9)
# 			b= xor(p_value,a)
# 			fake_block[7] = b
# 			a = xor(p10,c10)
# 			b= xor(p_value,a)
# 			fake_block[6] = b
# 			a = xor(p11,c11)
# 			b= xor(p_value,a)
# 			fake_block[5] = b		
# 			p7dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,fake_block2)
# 			break


# def p7dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,fake_block2):
# 	for i in range(0,256):
# 		fake_block[4] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[4]
# 			p_value = 12
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p12 = c2.decode("hex")
# 			print("Plaintext value of p5 "+str(p12))
# 			p_value = 13
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			c4 = fake_block2[12]
# 			c5 = fake_block2[11]
# 			c6 = fake_block2[10]
# 			c7 = fake_block2[9]
# 			c8 = fake_block2[8]
# 			c9 = fake_block2[7]
# 			c10 = fake_block2[6]
# 			c11 = fake_block2[5]
# 			c12 = fake_block2[4]

# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			a = xor(p4,c4)
# 			b= xor(p_value,a)
# 			fake_block[12] = b
# 			a = xor(p5,c5)
# 			b= xor(p_value,a)
# 			fake_block[11] = b	
# 			a = xor(p6,c6)
# 			b= xor(p_value,a)
# 			fake_block[10] = b
# 			a = xor(p7,c7)
# 			b= xor(p_value,a)
# 			fake_block[9] = b
# 			a = xor(p8,c8)
# 			b= xor(p_value,a)
# 			fake_block[8] = b
# 			a = xor(p9,c9)
# 			b= xor(p_value,a)
# 			fake_block[7] = b
# 			a = xor(p10,c10)
# 			b= xor(p_value,a)
# 			fake_block[6] = b
# 			a = xor(p11,c11)
# 			b= xor(p_value,a)
# 			fake_block[5] = b	
# 			a = xor(p12,c12)
# 			b= xor(p_value,a)
# 			fake_block[4] = b	
# 			p6dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,fake_block2)
# 			break
# def p6dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,fake_block2):
# 	for i in range(0,256):
# 		fake_block[3] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[3]
# 			p_value = 13
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p13 = c2.decode("hex")
# 			print("Plaintext value of p4 "+str(p13))
# 			p_value = 14
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			c4 = fake_block2[12]
# 			c5 = fake_block2[11]
# 			c6 = fake_block2[10]
# 			c7 = fake_block2[9]
# 			c8 = fake_block2[8]
# 			c9 = fake_block2[7]
# 			c10 = fake_block2[6]
# 			c11 = fake_block2[5]
# 			c12 = fake_block2[4]
# 			c13 = fake_block2[3]


# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			a = xor(p4,c4)
# 			b= xor(p_value,a)
# 			fake_block[12] = b
# 			a = xor(p5,c5)
# 			b= xor(p_value,a)
# 			fake_block[11] = b	
# 			a = xor(p6,c6)
# 			b= xor(p_value,a)
# 			fake_block[10] = b
# 			a = xor(p7,c7)
# 			b= xor(p_value,a)
# 			fake_block[9] = b
# 			a = xor(p8,c8)
# 			b= xor(p_value,a)
# 			fake_block[8] = b
# 			a = xor(p9,c9)
# 			b= xor(p_value,a)
# 			fake_block[7] = b
# 			a = xor(p10,c10)
# 			b= xor(p_value,a)
# 			fake_block[6] = b
# 			a = xor(p11,c11)
# 			b= xor(p_value,a)
# 			fake_block[5] = b	
# 			a = xor(p12,c12)
# 			b= xor(p_value,a)
# 			fake_block[4] = b
# 			a = xor(p13,c13)
# 			b= xor(p_value,a)
# 			fake_block[3] = b		
# 			p5dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,fake_block2)
# 			break

# def p5dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,fake_block2):
# 	for i in range(0,256):
# 		fake_block[2] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[2]
# 			p_value = 14
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p14 = c2.decode("hex")
# 			print("Plaintext value of p3 "+str(p14))
# 			p_value = 15
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			c4 = fake_block2[12]
# 			c5 = fake_block2[11]
# 			c6 = fake_block2[10]
# 			c7 = fake_block2[9]
# 			c8 = fake_block2[8]
# 			c9 = fake_block2[7]
# 			c10 = fake_block2[6]
# 			c11 = fake_block2[5]
# 			c12 = fake_block2[4]
# 			c13 = fake_block2[3]
# 			c14 = fake_block2[2]



# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			a = xor(p4,c4)
# 			b= xor(p_value,a)
# 			fake_block[12] = b
# 			a = xor(p5,c5)
# 			b= xor(p_value,a)
# 			fake_block[11] = b	
# 			a = xor(p6,c6)
# 			b= xor(p_value,a)
# 			fake_block[10] = b
# 			a = xor(p7,c7)
# 			b= xor(p_value,a)
# 			fake_block[9] = b
# 			a = xor(p8,c8)
# 			b= xor(p_value,a)
# 			fake_block[8] = b
# 			a = xor(p9,c9)
# 			b= xor(p_value,a)
# 			fake_block[7] = b
# 			a = xor(p10,c10)
# 			b= xor(p_value,a)
# 			fake_block[6] = b
# 			a = xor(p11,c11)
# 			b= xor(p_value,a)
# 			fake_block[5] = b	
# 			a = xor(p12,c12)
# 			b= xor(p_value,a)
# 			fake_block[4] = b
# 			a = xor(p13,c13)
# 			b= xor(p_value,a)
# 			fake_block[3] = b	
# 			a = xor(p14,c14)
# 			b= xor(p_value,a)
# 			fake_block[2] = b		
# 			p4dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,fake_block2)
# 			break


# def p4dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,fake_block2):
# 	for i in range(0,256):
# 		fake_block[1] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[1]
# 			p_value = 15
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p15 = c2.decode("hex")
# 			print("Plaintext value of p2 "+str(p15))
# 			p_value = 16
# 			c1 = fake_block2[15]
# 			c2 = fake_block2[14]
# 			c3 = fake_block2[13]
# 			c4 = fake_block2[12]
# 			c5 = fake_block2[11]
# 			c6 = fake_block2[10]
# 			c7 = fake_block2[9]
# 			c8 = fake_block2[8]
# 			c9 = fake_block2[7]
# 			c10 = fake_block2[6]
# 			c11 = fake_block2[5]
# 			c12 = fake_block2[4]
# 			c13 = fake_block2[3]
# 			c14 = fake_block2[2]
# 			c15 = fake_block2[1]





# 			a = xor(p1,c1)
# 			b= xor(p_value,a)
# 			fake_block[15] = b
# 			a = xor(p2,c2)
# 			b= xor(p_value,a)
# 			fake_block[14] = b
# 			a = xor(p3,c3)
# 			b= xor(p_value,a)
# 			fake_block[13] = b
# 			a = xor(p4,c4)
# 			b= xor(p_value,a)
# 			fake_block[12] = b
# 			a = xor(p5,c5)
# 			b= xor(p_value,a)
# 			fake_block[11] = b	
# 			a = xor(p6,c6)
# 			b= xor(p_value,a)
# 			fake_block[10] = b
# 			a = xor(p7,c7)
# 			b= xor(p_value,a)
# 			fake_block[9] = b
# 			a = xor(p8,c8)
# 			b= xor(p_value,a)
# 			fake_block[8] = b
# 			a = xor(p9,c9)
# 			b= xor(p_value,a)
# 			fake_block[7] = b
# 			a = xor(p10,c10)
# 			b= xor(p_value,a)
# 			fake_block[6] = b
# 			a = xor(p11,c11)
# 			b= xor(p_value,a)
# 			fake_block[5] = b	
# 			a = xor(p12,c12)
# 			b= xor(p_value,a)
# 			fake_block[4] = b
# 			a = xor(p13,c13)
# 			b= xor(p_value,a)
# 			fake_block[3] = b	
# 			a = xor(p14,c14)
# 			b= xor(p_value,a)
# 			fake_block[2] = b	
# 			a = xor(p15,c15)
# 			b= xor(p_value,a)
# 			fake_block[1] = b	
# 			p3dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,fake_block2)
# 			break

# def p3dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,fake_block2):
# 	for i in range(0,256):
# 		fake_block[0] = chr(i)
# 		temp = listToString(fake_block)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			print(a)
# 			c_dash = chr(i) #.encode("hex") # c'
# 			c_value = fake_block2[0]
# 			p_value = 15
# 			c = xor(c_dash,c_value)
# 			c2 = xor(p_value,c).encode("hex")
# 			p16 = c2.decode("hex")
# 			print("Plaintext value of p1 "+str(p16))
# 			break



	
# 			#p4dec(fake_block,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,fake_block2)
# 			break
# blocks,raw_blocks = splitblocks(iv_ct)

# # I am taking the '9th block which act as an xor for 10th block' as fake_block

# fake_block = list(raw_blocks[8])
# fake_block2 = raw_blocks[8]
# for i in range(0,1):
# 	#assert(i==)
# 	for j in range(190,200):
# 		temp = fake_block
# 		temp[15-i] = chr(j)
# 		temp = listToString(temp)
# 		temp = temp.encode("hex")
# 		b = blocks[0]+blocks[1]+blocks[2]+blocks[3]+blocks[4]+blocks[5]+blocks[6]+blocks[7]+temp+blocks[9]
# 		io.sendline(b)
# 		a = str(io.recvline())
# 		io.recvline()
# 		if "Invalid Padding" in a:
# 			continue
# 		else:
# 			if (chr(j)==fake_block2[15-i]):
# 				print("No")
# 			else:

# 				print(a)
# 				c_dash = chr(j) #.encode("hex") # c'
# 				c_value = fake_block2[15-i]
# 				p_value = i+1 # p
# 				c = xor(c_dash,c_value)
# 				c2 = xor(p_value,c).encode("hex")
# 				c2 = int(c2,16)
# 				print("Plaintext value of P16 "+str(c2))
# 				#[construction of the element]
# 				p2 = p_value+1
# 				final = xor(p2,c2)
# 				final = xor(final,c_value)
# 				fake_block[15-i] = final
# 				p17dec(fake_block,c2,fake_block2)
# 				break




















