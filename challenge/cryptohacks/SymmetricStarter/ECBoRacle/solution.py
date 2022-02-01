import requests
import time
import string
#http://aes.cryptohack.org/ecb_oracle/encrypt/

def splitblocks(c):
	order = len(c)/16
	chunks, chunk_size = len(c), len(c)/order
	a = [ c[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
	raw_blocks = a
	blocks = []
	for i in range(0,order):
		blocks.append(a[i].encode("hex"))
	return blocks
string_values = string.printable
temp =""
flag = ""
def recovery(matcher,a,temp,flag):
	for j in range(0,100):
		m = a + temp.encode("hex") + (string_values[j].encode("hex"))
		#print(m)
		send_request2 = "http://aes.cryptohack.org/ecb_oracle/encrypt/"+m
		y = requests.get(send_request2)
		ciphertext2 =y.text[15:-3]
		#time.sleep(1)
		blocks2 = splitblocks(ciphertext2.decode("hex"))
		matcher2 = blocks2[1]
		if(matcher == matcher2):		
			flag += string_values[j]

			temp = string_values[j]
			print("Recovered so far :"+flag)
			# temp = c
			return flag
			return temp

for i in range(1,32):
	# iiiiiiiiiiiiiiiiic
	a = "i"*(32-i)
	a = a.encode("hex")
	send_request = "http://aes.cryptohack.org/ecb_oracle/encrypt/"+a
	x = requests.get(send_request)
	ciphertext =x.text[15:-3]
	
	blocks = splitblocks(ciphertext.decode("hex"))
	matcher =blocks[1]
	#recovery(matcher,a,temp)
	temp += recovery(matcher,a,temp,flag)

			




#x = requests.get('http://aes.cryptohack.org/ecb_oracle/encrypt/')

#ciphertext = x.text
#crypto{p3n6u1n5_h473_3cb}
