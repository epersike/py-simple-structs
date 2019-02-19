class SimpleStackPopException(Exception):
	pass

class SimpleStackItem:
	def __init__(self, obj=None, prev=None, nxt=None):
		self.obj = obj
		self.prev = prev
		self.next = nxt

	def __str__(self):
		return str(self.obj)

class SimpleStack:
	def __init__(self):
		self.len = 0
		self.first = None
		self.s = None

	def add(self, obj):
		'''
			Add obj at the top of the stack.
		'''
		newObj = SimpleStackItem(obj)

		if self.first == None:
			self.first = self.s = newObj
		else:
			self.first.prev = newObj
			newObj.next = self.first
			self.first = newObj

		self.len += 1

	def is_empty(self):
		'''
			Returns false if the stack size is equal 0.
		'''
		return self.size() == 0

	def push(self, obj):
		'''
			Alias for 'SimpleStack.add'.
		'''
		self.add(obj)

	def pop(self):
		'''
			Return the last(est) item stacked.
		'''
		
		if self.first is None:
			raise SimpleStackPopException('Empty stack.')

		item = self.first.obj
		self.first = self.first.next 
		self.len -= 1

		return item	

	def __len__(self):
		'''
			Returns the length of the list.
		'''
		return self.len

	def size(self):
		'''
			Alias for 'Queue.__len__'.
			Returns the length of the list.
		'''
		return self.__len__()

	def __str__(self):
		'''
			Shows the content of queued objects.
		'''

		ret = ''
		obj = self.first

		while obj is not None:
			ret += str(obj)
			
			obj = obj.next

			if obj is not None:
				ret += ' -> '

		return ret
