
class HashTable:

	def __init__(self, size):
		self.data = list([0] * size)

	def _hash(self, key):
		hash = 0
		for i in range(len(key)):
		# 	hash += (ord(key[i]) * i)
		# hash %= len(self.data)
			hash = (hash + ord(key[i]) + i) % len(self.data)
		return hash

	def set(self, key, value):
		loc = self._hash(key)
		if not self.data[loc]:	
			self.data[loc] = [[key, value]]
		else:
			self.data[loc].append([key, value])

	def get(self, key):
		loc = self._hash(key)
		if self.data[loc]:
			for item in self.data[loc]:
				if item[0] == key:
					return item[1]
		else:
			raise KeyError(key)

	def delete(self, key):
		loc = self._hash(key)
		self.data[loc] = 0



my_hash_table = HashTable(50)
my_hash_table.set('grapes', 10000)
print(my_hash_table.get('grapes'))
my_hash_table.set('pizza', 500)
print(my_hash_table.get('pizza'))
my_hash_table.set('pizza', 400)
print(my_hash_table.get('pizza'))
my_hash_table.delete('grapes')
print(my_hash_table.get('grapes'))
