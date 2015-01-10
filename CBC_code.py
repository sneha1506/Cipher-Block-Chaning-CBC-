#!/usr/bin/env python

import hashlib,random
from Crypto.Cipher import AES
import time

# This method converts given key to 32-byte key
def ConvertKey_to_32_byte(key):
    Converted_key = hashlib.sha256(key).digest()
    return Converted_key;

# This method converts the message or input strings to a multiple of 16 in length
def Message_padding(message):
    Message_length = len(message)
    
    remainder = Message_length%16
    
    if (remainder) !=0:
        Padding_length = 16-remainder
        message = message+" "*Padding_length
        
    return message

if __name__ == '__main__':
    in_file = 'in.txt'
    en_file = 'Encrypted_CBC.txt'
    de_file = 'Decrypted_CBC.txt'
    
    in_FH = open(in_file,'r')
    encrypt_FH = open(en_file, 'w')
    decrypt_FH = open(de_file, 'w')
    
    message = in_FH.read()
    key = 'This is a key12'
    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    
    print ("Encryption started :")
    encrypt_start = time.time()
    obj = AES.new(ConvertKey_to_32_byte(key), AES.MODE_CBC, iv)
    ciphertext = obj.encrypt(Message_padding(message))
    
    print("Encryption Time taken {} seconds".format(time.time()-encrypt_start))
    encrypt_FH.write(ciphertext)
    
    # print ciphertext
    print("Decryption Started:")
    decrypt_start = time.time()
    obj2 = AES.new(ConvertKey_to_32_byte(key), AES.MODE_CBC, iv)
    plaintext = obj2.decrypt(ciphertext)
    print("Decryption Time taken {} seconds".format(time.time()-decrypt_start))
    decrypt_FH.write(plaintext)
    
    # print plaintext
    print("Total Time taken for the AES:CBC mode algorithm to run is {} seconds:".format(time.time()-encrypt_start))
    decrypt_FH.close()
    encrypt_FH.close()
    in_FH.close()
    
