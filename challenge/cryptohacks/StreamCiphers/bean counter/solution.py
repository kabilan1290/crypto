import json
import requests
import pwn



r = requests.get("http://aes.cryptohack.org/bean_counter/encrypt/")

encrypted = json.loads(r.text)

encrypted = encrypted['encrypted'].decode("hex")

png_header = "89504e470d0a1a0a0000000d49484452".decode("hex")

encrypted_header = encrypted[:16]
key=""
for i in range(0,16):
	key+=pwn.xor(encrypted_header[i],png_header[i])

flag = pwn.xor(key,encrypted)

file = open("flag.png","w")

file.write(flag)