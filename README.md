# Cipher-Block-Chaning-CBC-
Python code for Block cipher in CBC Mode
Usage:-

The file Rc4_code encrypts the bible text(stored as in.txt) using rc4 algorithm.
The file CBC_code encrypts the bible text(stored as in.txt) using CBC mode of encryption.
The file CTR_code encrypts the bible text(stored as in.txt) using CTR mode of encryption and both the CBC and CTR modes uses the inbuilt AES encryption from “pycrypto” library.

Modules needed:-

The codes CBC and CTR modes of encryptions needs PyCrypto module to install it you can use the following commands in your terminal or command prompt

	sudo install pip (Command to install pip)
	pip install PyCrypto (Command to install Pycrypto)


How to run the file:-

Run the file using the command “python Rc4_code.py” and it creates two files Encrypted_Rc4.txt and Decryption_Rc4.txt in your current working directory

You can repeat the above step by replacing the file name with CBC_code.py and CTR_code.py to run the other two files. 

I have also included the encrypted and decrypted files in the code folder
