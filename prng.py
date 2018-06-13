from typing import Callable

from bytes_functions import add

class PRNGenerator:
	
	def __init__(self, seed: bytes = b'\0'):
		raise NotImplementedError('PRNGenerator is just an interface')
	
	def seed(self, seed: bytes):
		self._seed = seed

	def __iter__(self):
		raise NotImplementedError('PRNGenerator is just an interface')

	def __next__(self):
		raise NotImplementedError('PRNGenerator is just an interface')
		
class HashPRNGenerator(PRNGenerator):
	
	def __init__(self, hash_function: Callable[[bytes], bytes], seed: bytes = b'\0'):
		self.__hash_function = hash_function

	def __iter__(self):
		self.index = 0
		return self
	
	def __next__(self):
		result = self.__hash_function(add(self._seed, self.index))
		self.index += 1
		return result
		
		
	

		
