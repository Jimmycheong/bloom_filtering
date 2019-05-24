'''

'''


class BloomFilter():

	'''
	The class should take a DB repository too for actually 
	accessing the data itself.

	It should also take a hashing function.

	'''

	def __init__(self, dbRepo, hasher_1, hasher_2, bit_vector_size = 10):
		self.dbRepo = dbRepo
		self.hasher_1 = hasher_1 
		self.hasher_2 = hasher_2
		self.bit_vector = [0 for i in range(bit_vector_size)]
		self.bit_vector_size = bit_vector_size

	def validate_hashs(self, hash_1, hash_2) -> bool :

		'''
		Checks if the hashes are within range of the bit vector.
		'''
		if hash_1 > len(self.bit_vector) and hash_1 < 0 :
			return False 
		if hash_2 > len(self.bit_vector) and hash_2 < 0 :
			return False 
		return True

	def insert_new_data(self, key, value) -> bool: 

		'''
		Upon inserting new data, the bloom filter needs use both hashing
		functions and update the bit_vector.

		'''

		hash_1 = self.hasher_1.hash_key(key, self.bit_vector_size)
		hash_2 = self.hasher_2.hash_key(key, self.bit_vector_size)

		if self.validate_hashs(hash_1, hash_2): 
			self.update_bit_vector(hash_1, hash_2)
			self.__set_data_by_key(key, value)
		else:
			raise Exception("BAD HASHES")
		return True

	def update_bit_vector(self, hash_1, hash_2) -> bool :

		'''
		Updates the current bit vector.

		'''
		self.bit_vector[hash_1] = 1 
		self.bit_vector[hash_2] = 1 

		return True

	def __get_data_by_key(self, key):

		'''
		Uses bloom filter to check for existence of key.

		'''

		return self.dbRepo.get_data_by_key(key)

	def __set_data_by_key(self, key, value): 
		
		'''
		Calls the db repo to set the key-value pair.

		'''

		is_success = self.dbRepo.insert_data(key, value)

		if is_success is False:
			raise Exception("Error updating!")
		return True
		


