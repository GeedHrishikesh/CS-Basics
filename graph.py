from collections import defaultdict
class Graph:
    # initializes the graph
    def __init__(self):
        self.graph = defaultdict(dict)
    
    # add edge from node1, node2 with weight
    def addEdge(self, node1, node2, weight = 0):
        self.graph[node1][node2] = weight

    # create Graph with different functions 
    def setUnDirectedGraph(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1])
            self.addEdge(edge[1], edge[0])
    
    def setDirectedGraph(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1])

    def setWeightedUnDirectedGraph(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1], edge[2])
            self.addEdge(edge[1], edge[0], edge[2])
    
    def setWeightedDirectedGraph(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1], edge[2])

class DFS():
    def __init__(self, graph, nodes):
        self.Graph = graph 
        self.Nodes = nodes 
        self.visited = [False]*(nodes+1)
    
    def isCycle(self):
        ans = False
        for node,visited in enumerate(self.visited):
            if not visited:
                ans = ans or self.detectCycle(node)
                if ans == True:
                    return ans 
        return ans
            
    def detectCycle(self, node, parentnode = -1):
        self.visited[node] = True 
        ans = False
        for child_node in self.Graph.graph[node]:
            if child_node != parentnode :
                if self.visited[child_node] == True:
                    return True 
                else:
                    ans = ans or self.detectCycle(child_node, node)
        self.visited[node] = False
        return ans

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        graph = Graph()
        graph.setUnDirectedGraph(B)

        dfsSearcher = DFS(graph, A)
        if dfsSearcher.isCycle():
            return 1
        else:
            return 0