
class Sdj:
	
	def __init__(self, *arguments):
		self.representant,self.element = [],[]
		self.sets = 0
		for item in arguments:
			self.make_set(item)
		
	def __str__(self):
		result = ""
		for i in range(len(self.element)):
			result += str(self.representant[i]) + " " + str(self.element[i]) + "\n"
		return result
			
	def __del__(self):
		del self.representant
		del self.element
		del self.sets
	
	def __len__(self):
		return self.sets	

	def make_set(self,item):
		self.representant.append(item)
		self.element.append(item)
		self.sets +=1

	def find(self, item):
		for i in range(len(self.element)):
			if self.element[i] == item :
				return self.representant[i]
		self.make_set(item)
		return item
	
	def union(self, item1, item2):
		Rep1 = self.find(item1)
		Rep2 = self.find(item2)
		if Rep1 == Rep2 :
			return False
		for i in range(len(self.element)):
			if self.representant[i] == Rep1:
				self.representant[i] = Rep2
		self.sets -= 1
		return True

