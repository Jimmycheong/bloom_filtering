from src.bloom_filter import BloomFilter
from src.hashing_function import HashingFunction
from src.db_repository import BasicDBRepository
import pytest

BIT_VECTOR_SIZE = 5
DATA_KEY = 24
DATA_VALUE = "This is a value"

class SampleHasher(HashingFunction):

	"""
	Simple hasher that hashes by taking the modolo of a int key.
	"""

	def __init__(self): 
		pass 

	def hash_key(self, key, number): 
		return key % number

hashing_function = SampleHasher()

def test_insert_new_data_successfully():

	"""
	Tests insertion of new data into a new Bloom filter
	"""

	hash_functions = [hashing_function]
	db_repository = BasicDBRepository()
	bloom_filter = BloomFilter(db_repository,hash_functions,BIT_VECTOR_SIZE)

	bloom_filter.insert_new_data(DATA_KEY, DATA_VALUE)

	assert bloom_filter.bit_vector == [0,0,0,0,1]
	assert db_repository.show_data() == {DATA_KEY: DATA_VALUE}

def test_read_with_existing_key_successfully():

	hash_functions = [hashing_function]
	db_repository = BasicDBRepository()
	db_repository.data_map = {DATA_KEY: DATA_VALUE}
	bloom_filter = BloomFilter(db_repository,hash_functions,BIT_VECTOR_SIZE)
	bloom_filter.bit_vector = [0,0,0,0,1]

	result = bloom_filter.get_data_with_key(DATA_KEY)

	assert result == DATA_VALUE

def test__validate_hashs_success():

	bloom_filter = BloomFilter(None,[],BIT_VECTOR_SIZE)

	hash_= hashing_function.hash_key(DATA_KEY, BIT_VECTOR_SIZE)

	assert bloom_filter._validate_hashs([hash_]) == True

def test__validate_hashs_failure():

	bloom_filter = BloomFilter(None,[],BIT_VECTOR_SIZE)

	hash_= hashing_function.hash_key(DATA_KEY, BIT_VECTOR_SIZE)

	assert bloom_filter._validate_hashs([6]) == False

def test__check_key_existence_success():

	db_repository = BasicDBRepository()
	db_repository.data_map = {DATA_KEY: DATA_VALUE}
	bloom_filter = BloomFilter(db_repository,[],BIT_VECTOR_SIZE)
	bloom_filter.bit_vector = [0,0,0,0,1]

	hash_= hashing_function.hash_key(DATA_KEY, BIT_VECTOR_SIZE)

	assert bloom_filter._check_key_existence([hash_]) == True

def test__check_key_existence_failure():

	db_repository = BasicDBRepository()
	db_repository.data_map = {DATA_KEY: DATA_VALUE}
	bloom_filter = BloomFilter(db_repository,[],BIT_VECTOR_SIZE)
	bloom_filter.bit_vector = [0,0,0,0,0]

	hash_= hashing_function.hash_key(DATA_KEY, BIT_VECTOR_SIZE)

	assert bloom_filter._check_key_existence([hash_]) == False


def test__update_bit_vector():

	hashes = [4]
	bloom_filter = BloomFilter(None,[],BIT_VECTOR_SIZE)

	bloom_filter._update_bit_vector(hashes)

	assert bloom_filter.bit_vector == [0,0,0,0,1]
