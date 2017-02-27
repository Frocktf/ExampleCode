
# #use base64 to decode or encode
# import base64

# str1 = "Hello World"
# str2 = base64.b64encode(str1)
# print str2
# print base64.b64decode(str2)

#use win32com client to encode or decode string ,this function is just in windows

# import win32com.client
# def encrypt(key,content):
# 	'''
# 	Args:
# 	key: 
# 	content:
# 	'''
# 	EncyptedData = win32com.client.Dispatch("CAPICOM.EncyptedData")
# 	EncyptedData.Algorithm.KeyLength = 5
# 	EncyptedData.Algorithm.Name = 2
# 	EncyptedData.SetSercret(key)
# 	EncyptedData.Content = content
# 	return EncyptedData.Encrypt()

# def decrypt(key,content):
# 	'''
# 	Args:
# 	key:
# 	content:
# 	'''
# 	EncryptedData = win32com.client.Dispatch("CAPICOM.EncryptedData")
# 	EncryptedData.Algorithm.KeyLength = 5
# 	EncryptedData.Algorithm.Name = 2
# 	EncryptedData.SetSercret(key)
# 	EncryptedData.Decrypt(content)
# 	return EncryptedData.Content

# s1 = encrypt('lovebread','hello world')
# s2 = decrypt('lovebread',s1)
# print s1,s2

#AES Advanced Encryption Standard
#pip install pycrypto
# from Crypto.Cipher import AES
# obj = AES.new('This is a key123',AES.MODE_CBC,'This is an IV456')
# message = "The answer is no"
# ciphertext = obj.encrypt(message)
# print ciphertext
# obj2 = AES.new("This is a key123",AES.MODE_CBC,'This is an IV456')
# print obj2.decrypt(ciphertext)

#coding:utf-8
import sys
from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex

class prpcrypt:
	def __init__(self,key):
		self.key = key
		self.mode = AES.MODE_CBC

	#encoding function, if the text is must multiple of 16
	def encrypt(self,text):
		cryptor = AES.new(self.key,self.mode,self.key)
		#the length of key is must be 16(AES-128),24(AES-192),32(AES-256) bytes.
		length = 16
		count = len(text)
		add = length - (count%length)
		text = text + ('\0'*add)
		self.ciphertext = cryptor.encrypt(text)
		return b2a_hex(self.ciphertext)
	#decoding function
	def decrypt(self,text):
		cryptor = AES.new(self.key,self.mode,self.key)
		plain_text = cryptor.decrypt(a2b_hex(text))
		return plain_text.rstrip('\0')

if __name__ == '__main__':
	pc = prpcrypt('keyskeyskeyskeys')
	e = pc.encrypt('00000')
	d = pc.decrypt(e)
	print e,d
	e = pc.encrypt("0000000000000000000000")
	d = pc.decrypt(e)
	print e,d
		


