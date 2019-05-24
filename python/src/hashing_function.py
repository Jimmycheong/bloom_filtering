'''hashing_function.py

Contains some hashing function.

'''
import abc 

class HashingFunction():

	def __init__(self):
		pass
	@abc.abstractmethod
	def hash_key(key): 
		pass

class BasicHashingFunction(HashingFunction):

	'''
	Hashes a number ID to a number
	'''

	def __init__(self):
		pass

	def hash_key(self, key, range):

		return key % range

class Basic2HashingFunction():

	'''
	Hashes a number ID to a number
	'''

	def __init__(self):
		pass

	def hash_key(self, key, range_):
		
		return (key + 2) % range_