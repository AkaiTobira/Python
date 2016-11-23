class Customer:

	def __init__(self, data = None, next = None, indx = None):
		self.data = data
		self.next = next
		self.indx = indx 

	def __str__(self):
		return str(self.data)

	def __del__(self):
		del self.data
		del self.next
		del self.indx

class QueueError(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class Pro_Que:

	def __init__(self):
		self.head = None
		self.tem1 = None
		self.tem2 = None
		self.size = 0

	def __str__(self):
		res = ""
		if self.head == None :
			return res
		self.tem1 = self.head
		while not self.tem1.next == None:
			res += str( self.tem1.data ) + " "
			self.tem1 = self.tem1.next
		res += str( self.tem1.data ) + "\n"
		return res
	
	def __len__(self):
		return self.size
	
	def __del__(self):
		del self.tem1
		del self.tem2
		del self.head
	
	def is_empty(self):
		return not self.size

	def insert( self, value, index ):
		if self.head == None :
			self.head = Customer( value, None, index )
			self.size +=1
		else :
			if index < self.head.indx:
				if self.size >= 1:
					self.tem1 = self.head
					self.tem2 = self.head
					while not self.tem1.next == None:
						self.tem2 = self.tem1
						self.tem1 = self.tem1.next
						if self.tem1.indx < index:
							break
					if self.tem1.next == None and self.tem1.indx > index:
						self.tem1.next = Customer( value, None, index)
						self.size +=1
					else:
						self.tem2.next = Customer( value, None, index)
						if self.size == 1 :
							self.tem1 = None
						self.tem2.next.next = self.tem1
						self.size +=1
			else:
				self.tem1 = self.head
				self.head = Customer( value, self.tem1, index )
				self.size +=1

	def minimum(self):
		if self.head == None :
				raise QueueError("No elements in Queue")
		else:		
			self.tem1 = self.head
			self.tem2 = self.head
			for i in range(self.size):
				self.tem2 = self.tem1
				self.tem1 = self.tem1.next
			return self.tem2.data

	def maximum(self):
		if self.head == None :	
			raise QueueError("Empty Queue")
		else:
			return self.head.data

	
	def removeMin(self):
		temp = self.minimum()
		self.remove(temp)
		return temp

	def remove(self, value):
		if self.head == None :	
			raise QueueError("Empty Queue")
		else:
			self.tem1 = self.head
			self.tem2 = self.head
			while not self.tem1.next == None:
				if self.tem1.next == None :
					raise QueueError("No element in Queue")
				if self.tem1.data == value :
					break
				self.tem2 = self.tem1
				self.tem1 = self.tem1.next

			if self.tem1 == self.head :
				self.head = None
				self.size-=1
			else:
				self.tem2.next = self.tem1.next
				self.size-=1


