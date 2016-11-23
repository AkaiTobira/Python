
import sys
from random import randint
from pro_que import Pro_Que
from sdj import Sdj

class Lab_Graph :

	def __init__(self,H=1,L=1):
		self._used,self._briges = [],[]		
		self._hight = H
		self._lengh = L
		self.verticles = H*L 
		for i in range(self.verticles):
			self._briges.append([])
			self._used.append(False)
			for j in range(self.verticles):
				self._briges[i].append(False)
		
	
	def __str__(self):
		leb = "$ "
		
		for i in range(self._lengh-1):
			leb += "$$"
		leb += "$\n"

		numb = 0
		for i in range(self._hight):
			leb += "$"
			for j in range(self._lengh):
				leb += " "
				if not j == self._lengh-1:
					if self._briges[numb][numb+1] :
						leb += " "
						numb+=1
					else :
						leb += "$"
						numb+=1
				else :
					leb += "$"
			numb -= self._lengh-1
			leb += "\n"
			for j in range(self._lengh):
				if i != self._hight-1 :
					leb += "$"
					if self._briges[numb][numb+self._lengh] :
						leb += " "
						numb+=1
					else :
						leb += "$"
						numb+=1
				else:
					leb += "$$"
			leb = leb[0:len(leb)-1]
			leb += " $\n"
			
		return leb

	def AldousBroderGenerate(self):
	
		used = []
	
		for i in range(self.verticles):
			used.append(False)
			for j in range(self.verticles):
				self._briges[i][j] = False

		s = randint(0,self.verticles-1)
		used[s] = True
		end = 0
		while end != self.verticles -1 :
			ran = randint(0,3)	
			if ran == 0 :
				if s+1 < self.verticles and (s+1) % self._lengh != 0:
					if not used[s+1] :
						used[s+1] = True
						self._briges[s][s+1] = True
						end+=1
					s+=1
			elif ran == 1 :
				if s-1 >= 0 and s % self._lengh != 0 :
					if not used[s-1] :
						used[s-1] = True
						self._briges[s-1][s] = True
						end+=1 
					s-=1
			elif ran == 2 :
				if s + self._lengh < self.verticles :
					if not used[s + self._lengh] :
						used[s+ self._lengh] = True
						self._briges[s][s+ self._lengh] = True
						end+=1
					s += self._lengh
			elif ran == 3 :
				if s - self._lengh >= 0 :
					if not used[s - self._lengh] :
						used[s - self._lengh] = True
						self._briges[s- self._lengh][s] = True 
						end+=1
					s -= self._lengh


	def PrimGenerate(self):
		for i in range(self.verticles):
			for j in range(self.verticles):
				self._briges[i][j] = False	
		Que = Pro_Que()
		is_part  = []
		is_ready = []
		for i in range(self.verticles):
			is_part.append(False)
			is_ready.append(False)
		s = randint(0,self.verticles-1)
		k = (s,s)
		is_part[s] = True
		is_ready[s] = True
		Que.insert(k,9223372036854775807);
		while len(Que) != 0 :
			if k[0] + self._lengh < self.verticles:
				if not is_ready[k[0] + self._lengh]:
					Que.insert( (k[0],k[0]+self._lengh), randint(0,9223372036854775806) )
					is_ready[k[0]+self._lengh] = True
			if k[0] - self._lengh >= 0:
				if not is_ready[k[0] - self._lengh]:
					Que.insert( (k[0],k[0]-self._lengh), randint(0,9223372036854775806) )
					is_ready[k[0]-self._lengh] = True
			if k[0] - 1 >= 0 and ( k[0] % self._lengh != 0 or k[0] == 0 ):
				if not is_ready[k[0] - 1]:
					Que.insert( (k[0],k[0]-1), randint(0,9223372036854775806) )
					is_ready[k[0]-1] = True
			if k[0] + 1 <= self.verticles and ( k[0] % self._lengh != self._lengh-1 or k[0] == 0 ):
				if not is_ready[k[0] + 1]:
					Que.insert( (k[0],k[0] + 1), randint(0,9223372036854775806) )
					is_ready[k[0]+ 1] = True
			k = Que.removeMin()
			if not is_part[k[1]]:
				self._briges[k[0]][k[1]] = True
				self._briges[k[1]][k[0]] = True 
				is_ready[k[1]] = True
			k = (k[1],k[1])

	def KruskallGenerate(self):

		is_part  = []
		for i in range(self.verticles):
			is_part.append(False)
			for j in range(self.verticles):
				self._briges[i][j] = False
		
		SDJ = Sdj()

		for i in range(self.verticles):
			SDJ.make_set(i)

		s = randint(0,self.verticles-1)
		while len(SDJ) != 1 :
			is_part[s] = True
			if s + self._lengh < self.verticles:
				if not SDJ.find(s) == SDJ.find(s+self._lengh): 
					SDJ.union(s,s+self._lengh)
					self._briges[s][s+self._lengh] = True
			if s - self._lengh >= self.verticles:
				if not SDJ.find(s) == SDJ.find(s-self._lengh): 
					SDJ.union(s,s-self._lengh)
					self._briges[s-self._lengh][s] = True
			if s + 1 <= self.verticles and ( s%self._lengh != self._lengh-1 or s == 0 ):
				if not SDJ.find(s) == SDJ.find(s+1): 
					SDJ.union(s,s+1)
					self._briges[s][s+1] = True
			if s - 1 >= 0 and ( s%self._lengh != 0 or s == 0 ):
				if not SDJ.find(s) == SDJ.find(s-1): 
					SDJ.union(s,s-1)
					self._briges[s-1][s] = True
			while is_part[s] != False:
				s = randint(0,self.verticles-1)

		
