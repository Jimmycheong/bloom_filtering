"""Bloom filter logic"""


class BloomFilter():
	"""
	Bloom Filter

	The class should take a DB repository too for actually
	accessing the data itself.

	It should also take a hashing function.
	"""

	def __init__(self, dbRepo, hash_functions=[], bit_vector_size=10):

		self.dbRepo = dbRepo
		self.hash_functions = hash_functions
		self.bit_vector = [0 for i in range(bit_vector_size)]
		self.bit_vector_size = bit_vector_size

	def insert_new_data(self, key, value) -> bool:
		"""
		Upon inserting new data, the bloom filter needs use both hashing
		functions and update the bit_vector.
		"""
		# hash_1 = self.hasher_1.hash_key(key, self.bit_vector_size)
		# hash_2 = self.hasher_2.hash_key(key, self.bit_vector_size)


		hashes = list(map(lambda hf: hf.hash_key(key, self.bit_vector_size), self.hash_functions))

		if self._validate_hashs(hashes):
			self._update_bit_vector(hashes)
			self._set_data_by_key(key, value)
		else:
			raise Exception("BAD HASHES!")
		return True

	def get_data_with_key(self, key):
		"""
		Get's value from DB.
		"""
		hashes = list(map(lambda hf: hf.hash_key(key, self.bit_vector_size), self.hash_functions))

		if self._validate_hashs(hashes):
			print("Reached!")
			if self._check_key_existence(hashes):
				print("Reached! 2")
				return self._get_data_by_key(key)
		return None

	def _validate_hashs(self, hashes) -> bool :
		"""Checks if the hashes are within range of the bit vector."""

		def isWithinRange(num, min, max) -> bool:
			return False if num > max or num < 0 else True

		return all(list(map(lambda x: isWithinRange(x, 0, len(self.bit_vector)), hashes)))

	def _check_key_existence(self, hashes) -> bool: 
		"""Checks to see if bits exist in the filter's bit_vector"""

		return all(list(map(lambda h: self.bit_vector[h] == 1, hashes)))

	def _update_bit_vector(self, hashes) -> bool :
		"""Updates the current bit vector."""

		for h in hashes: 
			self.bit_vector[h] = 1

	def _get_data_by_key(self, key):
		"""Uses bloom filter to check for existence of key."""

		return self.dbRepo.get_data_by_key(key)

	def _set_data_by_key(self, key, value):
		"""Calls the db repo to set the key-value pair."""
		is_success = self.dbRepo.insert_data(key, value)

		if is_success is False:
			raise Exception("Error updating!")
		return True
