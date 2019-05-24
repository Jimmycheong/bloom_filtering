'''db_repository.py

Access to the data

'''
import abc 
from typing import Dict


class DBRepository(abc.ABC):

	def __init__(self):
		pass

	@abc.abstractmethod
	def get_data_by_key(self, key):
		pass

	@abc.abstractmethod
	def get_data_by_key(self, key, value):
		pass 


class BasicDBRepository(DBRepository): 

	def __init__(self):
		self.data_map = {}

	def get_data_by_key(self, key):
		if key in self.data_map: 
			return self.data_map[key]

	def insert_data(self, key, value) -> bool:

		if key in self.data_map: 
			return False 
		else: 
			self.data_map[key] = value
			return True

	def update_data(self, key, value) -> bool:

		if key not in self.data_map:
			return False 
		else:
			self.data_map[key] = value
			return True

	def show_data(self) -> Dict[int, str]: 
		return self.data_map
