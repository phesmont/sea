"""
Symmetric Encryption Algorithm based on prngs (and some hashing)
"""

from typing import List, Callable, Union, Generator

from prng import PRNGenerator
from bytes_functions import xor

		
def encrypt (message: bytes, key: bytes, prn_generator: PRNGenerator, hash_function: Callable[[bytes], bytes]) -> bytes:

	hash_of_message = hash_function(message)

	encrypted_message = hash_of_message

	prn_generator.seed(xor(hash_of_message, key))
	
	prn_iter = iter(prn_generator)
	
	for byte_pair in zip(message, (b for h in prn_iter for b in h)):
		encrypted_message += xor(byte_pair[0], byte_pair[1])
		
	return encrypted_message

def decrypt (cipher: bytes, key: bytes, prn_generator: PRNGenerator, hash_length: int):
	decrypted_message = b''

	hash_of_message = cipher[:hash_length]
	
	prn_generator.seed(xor(hash_of_message, key))
	
	prn_iter = iter(prn_generator)
	
	for byte_pair in zip(cipher[hash_length:], (b for h in prn_iter for b in h)):
		decrypted_message += xor(byte_pair[0], byte_pair[1])
	
	return decrypted_message

if __name__ == '__main__':
	from prng import HashPRNGenerator
	from hashfunctions import sha256_function as hash_function
	from sys import stderr, argv
	
	my_prng = HashPRNGenerator(hash_function)

	def print_usage():
		print('Usage: sea --encrypt <UTF-8 key>', file=stderr)
		print('       sea --decrypt <UTF-8 key>', file=stderr)
		print('Cipher and message to stdout/in ', file=stderr)
		exit(1)
	
	try:
		if argv[1] == '--encrypt' or argv[1] == '-e':
			message = bytes(input(), 'UTF-8')
			key = bytes(argv[2], 'UTF-8')
			cipher = encrypt(message, key, my_prng, hash_function)
			print(cipher.hex())
		elif argv[1] == '--decrypt' or argv[1] == '-d':
			cipher = bytes.fromhex(input())
			key = bytes(argv[2], 'UTF-8')
			plain = decrypt(cipher, key, my_prng, 32)
			print(plain.decode('UTF-8'))
		else:
			print_usage()
	except:
		print_usage()




