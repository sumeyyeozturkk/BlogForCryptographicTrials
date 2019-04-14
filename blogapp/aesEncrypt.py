from Crypto.Cipher import AES
import random, string, base64


def encrypt_text(key,encrypted_text):
	iv = 'YBK7Cp7kPem4dDWZ'
	enc_s = AES.new(key, AES.MODE_CFB, iv)
	cipher_text = enc_s.encrypt(encrypted_text.encode('utf-8'))
	encoded_cipher_text = base64.b64encode(cipher_text)
	return encoded_cipher_text


def decrypt_text(key,encoded_cipher_text):
	iv = 'YBK7Cp7kPem4dDWZ'
	decryption_suite = AES.new(key, AES.MODE_CFB, iv)
	plain_text = decryption_suite.decrypt(base64.b64decode(encoded_cipher_text))
	return plain_text.decode('utf-8')