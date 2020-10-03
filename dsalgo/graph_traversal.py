from collections import defaultdict
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	#Method to add an edge to the graph
	def addEdge(self, u ,v):
		self.graph[u].append(v)

	##perform dfs on the graph using queue
	def bfs(self, s):
		##Visited list to keep track of elements we have already visited
		visited = []
		##List to store the neighbours of a node
		queue = []
		##List to store the ans
		ans = []
		queue.append(s)
		visited.append(s)
		while queue:
			s = queue.pop(0)
			ans.append(s)
			for i in self.graph[s]:
				if i not in visited:
					queue.append(i)
					visited.append(i)
		##Return the ans list
		return ans

	##Perform dfs using recursion
	def dfs(self, s, visited=None, ans=None):
		#If visited list is empty create one
		if visited is None:
			visited = [] 
		##Add the current node to the visited array
		visited.append(s)
		if ans is None:
			ans = []
		ans.append(s)
		for i in self.graph[s]:
			if i not in visited:
				self.dfs(i, visited, ans)
		##Return the ans list
		return ans