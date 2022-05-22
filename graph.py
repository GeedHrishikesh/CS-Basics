from collections import defaultdict
import heapq

class Graph:
    # initializes the graph
    def __init__(self,nodes):
        self.graph = defaultdict(dict)
        self.nodes = nodes
        self.visited = [False]*nodes
        self.degrees = [0]*self.nodes
    
    # add edge from node1, node2 with weight
    def addEdge(self, node1, node2, weight = 0):
        self.graph[node1][node2] = min(weight,self.graph[node1].get(node2,float("inf")))
        self.degrees[node2-1] += 1

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

    def topologicalSort(self):
        heap = []

        for node in range(self.nodes):
            heapq.heappush(heap,(self.degrees[node], node))
        
        while(heap):
            degree, node = heapq.heappop(heap)
            if not self.visited[node] and degree > 0 :
                return False
            if not self.visited[node]:
                self.visited[node] = True
                for child_node in self.graph[node]:
                    self.degrees[child_node] -= 1 
                    heapq.heappush(heap, (self.degrees[child_node], child_node))
        return True

    def getMSTWeight(self):
        heap = []
        heapq.heappush(heap,(0,1))
        ans = 0
        while(heap):
            weight, node = heapq.heappop(heap)
            if self.visited[node-1] == False:
                self.visited[node-1] = True 
                ans = ans + weight
                for child_node in self.graph[node]:
                    if self.visited[child_node-1] == False:
                        heapq.heappush(heap,(self.graph[node][child_node], child_node))
        if False in self.visited:
            return -1
        else:
            return ans

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

class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = Graph(n)
        graph.setWeightedUnDirectedGraph(connections)
        return graph.getMSTWeight()
        
