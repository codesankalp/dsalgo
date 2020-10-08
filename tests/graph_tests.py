from dsalgo.graph_traversal import Graph

mat = [
    [1, 3],
    [1, 5],
    [1, 6],
    [2, 5],
    [2, 6],
    [3, 4],
    [3, 5],
    [5, 6],
    [7, 6],
    [9, 8],
    [8, 10],
    [9, 4],
    [4, 8],
    [10, 2]]

g = Graph()
b = Graph()
#Test for directed graph
for i in mat:
    g.addEdge(i[0], i[1])
    b.addEdge(i[0], i[1])
    b.addEdge(i[1], i[0])


#Print the results for directed graph
print(g.bfs(2))
print(g.dfs(9))

#Print the results for undirected graph
print(b.bfs(2))
print(b.dfs(9))

