#!/usr/bin/python
# -*- coding: utf-8 -*-
#

class Sdj:
	""" Niewykorzystywana implementacja """
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

class UnionFind:
    """ Implementacja Lasu zbiorów rozłącznych wg. Cormena'a """


    def __init__(self):
        self.parent = {}
        self.rank = {}
	self.l = 0

    def __str__(self):
	return str(self.parent)

    def __len__(self):
	return self.l

    def create(self, x):
        # Tworzymy drzewa jednoelementowe.
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
	    self.l+=1

    def find(self, x):
        # Szukamy korzenia drzewa.
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])   # kompresja
        return self.parent[x]

    def union(self, x, y):
        # Szukamy korzeni drzew.
        x = self.find(x)
        y = self.find(y)
        if x == y:   # to samo drzewo
            return False
        # Mniejsze drzewo podłączamy do większego.
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] = self.rank[y] + 1
	self.l-=1
	return True


