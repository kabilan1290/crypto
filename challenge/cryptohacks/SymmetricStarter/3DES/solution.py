import requests
import json

KEY = b"\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"#key = bytes.fromhex(key)
KEY = KEY.encode("hex")

#http://aes.cryptohack.org/triple_des/encrypt_flag/

encrypt = requests.get("http://aes.cryptohack.org/triple_des/encrypt_flag/"+KEY)

x = json.loads(encrypt.text)

cipher = x["ciphertext"]

# http://aes.cryptohack.org/triple_des/encrypt/+key/+pt

decrypt = requests.get("http://aes.cryptohack.org/triple_des/encrypt/"+KEY+"/"+cipher)

x = json.loads(decrypt.text)

plain = x["ciphertext"]

print("The flag is "+plain.decode("hex")[:34])
