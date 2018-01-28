class Vertex:
	"Initializes the Vertex class"
	def __init__(self,ident):
		self.id = ident
		self.connected_to = []
		self.visited = False

class MyGraph:
	"Initializes the MyGraph class, imports info from a file to build a graph"
	def __init__(self,filename):
		f = open(filename,'r')

		self.vert_list = {}
		self.num_verts = int(f.readline())
		self.num_edges = int(f.readline(2))
		
		for vert in range(1,self.num_verts + 1):
			new_vert = Vertex(vert)
			self.vert_list[vert] = new_vert

		for line in f:
			edge = line.split()
			vert1 = int(edge[0])
			vert2 = int(edge[1])

			self.vert_list[vert1].connected_to.append(vert2)
			self.vert_list[vert2].connected_to.append(vert1)

	def conn_components(self):
		"Returns a list of lists of all connected components"
		connected_list = []

		for vert in self.vert_list:
			if self.vert_list[vert].visited == False:
				connected_list.append(sorted(self.find_cons(vert)))

		return connected_list

	def find_cons(self,start_vert):
		"Recursive function to find connected components"
		returnlist = []
		self.vert_list[start_vert].visited = True

		returnlist += [self.vert_list[start_vert].id]

		if len(self.vert_list[start_vert].connected_to) == 0:
			return [self.vert_list[start_vert].id]

		if self.visited_nodes(self.vert_list[start_vert].connected_to):
			return [self.vert_list[start_vert].id]

		for nextVert in self.vert_list[start_vert].connected_to:
			if self.vert_list[nextVert].visited == False:
				returnlist += self.find_cons(nextVert)

		return returnlist


	def visited_nodes(self,edgelist):
		"Helper funciton to determine if all connections have been visited"

		allvisited = True

		for vert in edgelist:
			if self.vert_list[vert].visited == False:
				allvisited = False

		return allvisited

	def bicolor(self):
		"Function to test if a graph is biparite"

		v1 = []
		v2 = []
		bicolor = True

		for vert in self.vert_list:
			if self.vert_list[vert].id not in v1 and self.vert_list[vert].id not in v2:
				v1.append(self.vert_list[vert].id)
				v2 += self.vert_list[vert].connected_to

			elif self.vert_list[vert].id in v1:
				for adjvert in self.vert_list[vert].connected_to:
					if adjvert in v2:
						continue
					else:
						v2.append(adjvert)

			elif self.vert_list[vert].id in v2:
				for adjvert in self.vert_list[vert].connected_to:
					if adjvert in v1:
						continue
					else:
						v1.append(adjvert)

		for vert in v1:
			if vert in v2:
				bicolor = False

		return bicolor







# test = MyGraph('graphtest.txt')
# #print test.num_edges
# print test.conn_components()
# print test.bicolor()






