'''

'''

class BloomFilter():

	'''
	The class should take a DB repository too for actually 
	accessing the data itself.

	It should also take a hashing function.

	'''

	def __init__(self, size, hasher_1, hasher_2):
		self.hasher_1 = hasher_1 
		self.hasher_2 = hasher_2
		self.bit_vector = [0 for i in range(size)]

	def insert_new_data(key): 

		'''
		Upon inserting new data, the bloom filter needs use both hashing
		functions and update the bit_vector.

		'''

		hash_1 = self.hasher_1.hash(key)
		hash_2 = self.hasher_2.hash(key)

		update_bit_vector(hash_1, hash_2)
		pass

	def update_bit_vector(hash_1, hash_2):

		'''
		Updates the current bit vector.
		'''
		
		pass