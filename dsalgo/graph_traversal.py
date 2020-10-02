from collections import defaultdict
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u ,v):
		self.graph[u].append(v)

	def bfs(self, s):
		visited = [False] * (len(self.graph)+1)
		queue = []
		ans = []
		queue.append(s)
		visited[s] = True
		while queue:
			s = queue.pop(0)
			ans.append(s)
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True
		return ans

	def dfs(self, s, visited=None, ans=None):
		if visited is None:
			visited = [False] * (len(self.graph)+1)
		visited[s] = True
		if ans is None:
			ans = []
		ans.append(s)
		for i in self.graph[s]:
			if visited[i] == False:
				self.dfs(i, visited, ans)
		return ans