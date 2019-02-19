
class SimpleQueueDequeueException(Exception):
	pass

class SimpleQueueItem:
	def __init__(self, obj=None, prev=None, nxt=None):
		self.obj = obj
		self.prev = prev
		self.next = nxt

	def __str__(self):
		return str(self.obj)

class SimpleQueue:
	def __init__(self):
		self.len = 0
		self.first = None
		self.q = None

	def add(self, obj):
		'''
			Add obj to the end of the queue.
		'''
		newObj = SimpleQueueItem(obj)

		if self.first == None:
			self.first = self.q = newObj
		else:
			self.q.next = newObj
			newObj.previous = self.q
			self.q = newObj

		self.len += 1


	def dequeue (self):
		'''
			Return the first(est) item queued.
		'''
		
		if self.first is None:
			raise SimpleQueueDequeueException('Empty queue.')

		item = self.first.obj
		self.first = self.first.next 
		self.len -= 1

		return item	

	def is_empty(self):
		'''
			Returns false if the queue size is equal 0.
		'''
		return self.size() == 0

	def push(self, obj):
		'''
			Alias for 'SimpleQueue.add'.
		'''
		self.add(obj)

	def pop(self):
		'''
			Alias for 'SimpleQueue.dequeue'.
		'''
		return self.dequeue()

	def __len__(self):
		'''
			Returns the length of the list.
		'''
		return self.len

	def size(self):
		'''
			Alias for 'SimpleQueue.__len__'.
			Returns the length of the list.
		'''
		return len(self)

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
