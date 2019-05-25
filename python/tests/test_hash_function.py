'''
Tests for hashing functions.

'''

import pytest
from src.hashing_function import BasicHashingFunction, Basic2HashingFunction

def test_basic_hashing_function_hash_key():
	'''
	Should take the modulus of the key and return a value
	'''

	key = 14 
	range_ = 10
	expected_answer = 4

	basic_hash_function = BasicHashingFunction()

	assert basic_hash_function.hash_key(key, range_) == expected_answer
