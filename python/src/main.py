"""
Entry point for using bloom filter
"""
from pprint import pprint
from bloom_filter import BloomFilter
from db_repository import DBRepository, BasicDBRepository
from hashing_function import HashingFunction, BasicHashingFunction, Basic2HashingFunction

def main():

	"""
	- Access to the Database
	- Access to a Bloom filter
	- Consumer sending request for data

	"""

	UNIQUE_SET_SIZE = 5

	data_key = 34
	data_value = "This is a value"

	db_repository = BasicDBRepository()
	hashing_function_1 = BasicHashingFunction()
	hashing_function_2 = Basic2HashingFunction()

	print("Hello world!!")

	bloom_filter = BloomFilter(db_repository,hashing_function_1, hashing_function_2, UNIQUE_SET_SIZE)
	
	print(f'Initialized bloom filter: {bloom_filter.bit_vector}')

	bloom_filter.insert_new_data(data_key, data_value)

	print("Reached!")
	pprint(f"BloomFilter state: {bloom_filter.bit_vector}")
	pprint(db_repository.show_data(), width = 1)


if __name__ == '__main__':
	main() 
