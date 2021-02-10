import networkx as nx
import matplotlib.pyplot as plt
import sys
import numpy as np

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
        self.matrix = [[0 for column in range(V)]  
                     for row in range(V)] 

    def addEdge(self, u, v): 
            self.adj[u].append(v) 
            self.adj[v].append(u)

    def adjToMatrix(self):
        for i in range(len(self.adj)):
            for j in self.adj[i]:
                self.matrix[i][j] = self.matrix[j][i] = 1 
    def DFSUtil(self, temp, v, visited):
        visited[v] = True
        temp.append(v) 
  
        for i in self.adj[v]: 
            if visited[i] == False:
                temp = self.DFSUtil(temp, i, visited)
        return temp

    def connectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc
    

    def isCyclic(self, v, visited, parent): 
        visited[v] = True

        for i in self.adj[v]:
            if visited[i] == False:
                if self.isCyclic(i, visited, v) == True: 
                    return True

            elif i != parent: 
                return True
  
        return False

    def isTree(self, u):
        visited = [False] * self.V

        if self.isCyclic(u, visited, -1) == True: 
            return False

        return True

    def isForest(self):
        count = 0
        cc = self.connectedComponents()
        for i in cc:
            if self.isTree(i[0]) == False:
                return False
        return True


    def DFStree(self, start, visited):
        visited[start] = True
        print(start)
        for i in range(len(self.matrix)):
            if self.matrix[start][i] == 1 and not visited[i]:
                self.DFStree(i, visited)

    def BFS(self, start):
        visited = [False] * (self.V)
        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            start = queue.pop(0)
            print(start)
            for i in self.adj[start]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True


    def printMST(self, parent): 
        print("Edge \tWeight")
        for i in range(1, self.V): 
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]]) 
  
    def minKey(self, key, mstSet): 

        min = 999999 
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 

    def primMST(self): 
        key = [999999] * self.V 
        parent = [None] * self.V
        key[0] = 0 
        mstSet = [False] * self.V 
  
        parent[0] = -1 
  
        for cout in range(self.V): 
            u = self.minKey(key, mstSet) 
            mstSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
  
        self.printMST(parent)

    def printSolution(self, dist): 
        print ("Vertex total distance from Source") 
        for node in range(self.V): 
            print (node, "total", dist[node]) 

    def minDistance(self, dist, sptSet): 
 
        min = 99999

        min_index = 0

        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
   
        return min_index

    def dijkstra(self, src): 
        dijkstraList = [10000] * self.V 
        sptSet = [False] * self.V 
   
        for cout in range(self.V): 
            u = self.minDistance(dijkstraList, sptSet) 
   
            sptSet[u] = True
   
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dijkstraList[v] > dijkstraList[u] + self.graph[u][v]: 
                    dijkstraList[v] = dijkstraList[u] + self.graph[u][v] 
   
        self.printSolution(dijkstraList)
if __name__=="__main__":
    g = Graph(5) 
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(4, 2)
    g.graph = [ [0, 2, 0, 6, 0], 
                [2, 0, 3, 8, 5], 
                [0, 3, 0, 0, 7], 
                [6, 8, 0, 0, 9], 
                [0, 5, 7, 9, 0]]
    n = g.connectedComponents()
    print("thanh phan lien thong ", len(n))
    if g.isForest() == True:
        print("do thi nay la rung")
    else:
        print("ko phai rung")
    g.adjToMatrix()
    visited = [False] * g.V
    print(" using DFS")
    g.DFStree(0, visited)
    print(" using BFS")
    g.BFS(0)
    g.primMST()
    g.dijkstra(0)
    

