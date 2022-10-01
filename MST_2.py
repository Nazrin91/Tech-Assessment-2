# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph 

from collections import defaultdict
from unittest import result 

#Class to represent a graph 
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = [] # default dictionary 
								# to store graph 
		

	# function to add an edge to graph 
	def addEdge(self,u,v,w): 
		self.graph.append([u,v,w]) 

	# A utility function to find set of an element i 
	# (uses path compression technique) 
	def find(self, parent, i): 
		if parent[i] == i: 
			return i 
		return self.find(parent, parent[i]) 

	# A function that does union of two sets of x and y 
	# (uses union by rank) 
	def union(self, parent, rank, x, y): 
		xroot = self.find(parent, x) 
		yroot = self.find(parent, y) 

		# Attach smaller rank tree under root of 
		# high rank tree (Union by Rank) 
		if rank[xroot] < rank[yroot]: 
			parent[xroot] = yroot 
		elif rank[xroot] > rank[yroot]: 
			parent[yroot] = xroot 

		# If ranks are same, then make one as root 
		# and increment its rank by one 
		else : 
			parent[yroot] = xroot 
			rank[xroot] += 1

	# The main function to construct MST using Kruskal's 
		# algorithm 
	def KruskalMST(self): 

		result =[] #This will store the resultant MST 

		i = 0 # An index variable, used for sorted edges 
		e = 0 # An index variable, used for result[] 

			# Step 1: Sort all the edges in non-decreasing 
			 
		self.graph = sorted(self.graph,key=lambda item: item[2]) 

		parent = [] ; rank = [] 

		# Create V subsets with single elements 
		for node in range(self.V): 
			parent.append(node) 
			rank.append(0) 
	
		# Number of edges to be taken is equal to V-1 
		while e < self.V -1 : 

			# Step 2: Pick the smallest edge and increment 
					# the index for next iteration 
			u,v,w = self.graph[i] 
			i = i + 1
			x = self.find(parent, u) 
			y = self.find(parent ,v) 

			# If including this edge doesn't cause cycle, 
						# include it in result and increment the index 
						# of result for next edge 
			if x != y: 
				e = e + 1	
				result.append([u,v,w]) 
				self.union(parent, rank, x, y)			 
			# Else discard the edge 

		print(result)
	def __getitem__(self, key):
			return self.__dict__[key]

#Reading data from file
f = open("optical_network_input.txt", 'r', encoding='UTF-8')
lines = f.readlines()
lines.pop()

modified = []


for line in lines:

    if line[-1] == '\n':
        modified.append(line[:-1])
    else:
        modified.append(line)

s = set() # list all vertices
for ip in lines:
	s.add(ip.split(" ")[0])
	s.add(ip.split(" ")[1])

vertice = list(s)
g = Graph(len(vertice))

for ip in lines:
	a = ip.split(" ")[0]  #vertice 1
	b = ip.split(" ")[1]   #vertice 2
	w = int(ip.split(" ")[2])    #weight
	g.addEdge(vertice.index(a), vertice.index(b), w)

g.KruskalMST() 
