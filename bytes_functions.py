from typing import Iterable, Union

def to_bytes(b: int):
	return int.to_bytes(b, (int.bit_length(b) - 1) // 8 + 1, 'big')
	
def add(*addends: Iterable[Union[bytes, int]]) -> bytes:
	"""adds all the arguments (either of type bytes or int) and returns the sum"""
	result = 0
	for addend in addends:
		if type(addend) is bytes:
			 result += int.from_bytes(addend, 'big')
		else:
			result += addend
	return to_bytes(result)

def xor(*numbers: Iterable[Union[bytes, int]]) -> bytes:
	"""xors all the arguments (either of type bytes or int) and returns the result"""
	result = 0
	for number in numbers:
		if type(number) is bytes:
			 result ^= int.from_bytes(number, 'big')
		else:
			result ^= number
	return to_bytes(result)

