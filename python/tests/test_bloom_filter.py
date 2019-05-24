from src.bloom_filter import BloomFilter
from src.hashing_function import HashingFunction
from src.db_repository import BasicDBRepository
import pytest

UNIQUE_SET_SIZE = 5
data_key = 24
data_value = "This is a value"

class SampleHasher(HashingFunction):

	def __init__(self): 
		pass 

	def hash_key(self, key, number): 
		return key % number

db_repository = BasicDBRepository()
hashing_function_1 = SampleHasher()
hashing_function_2 = SampleHasher()

bloom_filter = BloomFilter(
	db_repository,
	hashing_function_1, 
	hashing_function_2, 
	UNIQUE_SET_SIZE
)


def test__insert_new_data():

	bloom_filter.insert_new_data(data_key, data_value)

	assert bloom_filter.bit_vector == [0,0,0,0,1]
	assert db_repository.show_data() == {data_key: data_value}