'''main.py

The following file is designed to create a bloom filter.

'''

from bloom_filter import BloomFilter

def main():

	'''
	- Access to the Database 
	- Access to a Bloom filter 
	- Consumer sending request for data
	
	'''

	UNIQUE_SET_SIZE = 5

	bloom_filter = BloomFilter(UNIQUE_SET_SIZE)


	print(bloom_filter.bit_vector)

	pass 


if __name__ == '__main__':
	main()