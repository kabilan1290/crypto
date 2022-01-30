import requests

x = requests.get('http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')

ciphertext = x.text


ciphertext = ciphertext[15:-3]

decryption = "http://aes.cryptohack.org/block_cipher_starter/decrypt/"+ciphertext

y = requests.get(decryption)

flag = y.text[14:-3].decode("hex")

if "crypto" in flag:
	print(flag)