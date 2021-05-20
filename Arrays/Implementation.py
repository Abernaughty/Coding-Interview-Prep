
class MyArray:
	def __init__(self, length = None):
		self.length = 0
		self.data = {}

	def __str__(self):
		return str(self.__dict__)

	def get(self, index):
		return self.data[index]

	def push(self, item):
		self.data[self.length] = item
		self.length += 1

	def pop(self, index = None):
		if index:
			item = self.data[index]
			for i in range(self.length - 1, index, -1):
				self.data[i - 1] = self.data[i]
			del self.data[self.length - 1]
		else:
			item = self.data[self.length - 1]
			del self.data[self.length - 1]
		self.length -= 1
		return item

	def insert(self, index, item):
		self.length += 1
		for i in range(self.length - 1, index, -1):
			self.data[i] = self.data[i - 1]
			self.data[index] = item

	def delete(self, index):
		# del self.data[index]
		for i in range(self.length - 1, index, -1):
			self.data[i - 1] = self.data[i]
		del self.data[self.length - 1]
		self.length -= 1


arr = MyArray()
arr.push('first')
print(arr.data)
arr.push('second')
print(arr.data)
arr.insert(1, 'third')
print(arr.data)
arr.push('fourth')
print(arr.pop(1))
print(arr.data)
arr.delete(1)
print(arr.length)
print(arr.data)
print(arr)

