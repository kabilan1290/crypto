cipher_text = raw_input("Enter cipher\n")

key = raw_input("key\n")

ct = cipher_text.decode("hex")


t = len(cipher_text)

t = int(t)

key = key * t

flag = "".join(chr(ord(i) ^ ord(j)) for i,j in zip(ct,key))

print(flag)


