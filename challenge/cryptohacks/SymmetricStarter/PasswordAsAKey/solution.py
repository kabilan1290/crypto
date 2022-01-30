import random
import hashlib
import requests
from Crypto.Cipher import AES 
with open("/usr/share/dict/words") as f:
    words = [w.strip() for w in f.readlines()]
    for word in words:
		try:
			key = hashlib.md5(word.encode()).digest()
			ct ="c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66".decode("hex")
			cipher = AES.new(key,AES.MODE_ECB).decrypt(ct)
			if "crypto" in cipher:
				print(cipher)
				print(word)
		except:
			continue