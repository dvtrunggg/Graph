import numpy as np
import networkx as nx
import os
import matplotlib.pyplot as plt



# yeu cau 1:
def getMatrix():
    with open('graph1.txt') as graph:
        n = graph.readline()
        matrix = np.array
        matrix = [[int(num) for num in line.split(' ')] for line in graph]

    print(n)
    for i in range(np.shape(matrix)[0]):
        count = 0
        for j in range(np.shape(matrix)[1]):
            if (matrix[i][j] == 1):
                count+=1
        print(count, end=' ')
        for j in range(np.shape(matrix)[1]):
            if (matrix[i][j] == 1):
                print(j, end=' ')
        print(end='\n')

#yeu cau 2 
def getList():
    with open('graph2.txt') as graph:
        n = graph.readline()
        n = int(n)
        list = np.array
        list = [[int(num) for num in line.split(' ')] for line in graph]
    matrix = np.empty(shape=(n,n), dtype = int)
    matrix.fill(0)

    for i in range(0, n):
        for j in range(1, list[i][0]+1):
            matrix[i][list[i][j]] = 1
    return matrix

#ktra do thi vo huong: ktra matran ke doi xung qua duong cheo chinh 
def isUndirected():
    a = getList()
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return False
    return True
#so dinh:
def num_OfVertex():
    return len(getList())

#so canh 
def num_OfEdges():
    k = getList()
    n = len(k)
    num = 0
    if isUndirected() == True:      # do thi vo huong: 
        for i in range(n):
            for j in range(n):
                if k[i][j] == 1 & k[j][i] == 1:
                    num+=1
    else:
        for i in range(n):
            for j in range(n):
                if k[i][j] == 1:
                    num +=1

    return num


def degree_OfUnDirected():
    x = getList()
    n = len(x)
    d = np.empty(shape=(n,1), dtype = int)
    d.fill(0)
    count = 0
    for i in range(n):
        for j in range(n):
            if x[i][j] == 1:
                count+=1
        d[i][0] = count
        count = 0
    return d


def degree_OfDirected():
    x = getList()
    n = len(x)
    d = np.empty(shape=(n,2), dtype = int)
    d.fill(0)
    count1 = count2 = 0
    for i in range(n):
        for j in range(n):
            if x[i][j] == 1:
                count1+=1
            if x[j][i] == 1:
                count2+=1
        d[i][0] = count1
        d[i][1] = count2
        count1 = count2 = 0
    return d


#dinh co lap
def isIsolated():
    a = getList()
    n = len(a)
    iso = []

    if not isUndirected():
        d = degree_OfDirected()
        for i in range(n):
            if d[i][0] == 0 and d[i][1] == 0:
                iso.append(i)
    else:
        d = degree_OfUnDirected()
        for i in range(n):
            if d[i][0] == 0:
                iso.append(i)
    return iso

#dinh treo
def isPendant():
    pendant = degree_OfDirected()
    for i in range(len(pendant)):
        if (pendant[i][0] == 1 and pendant[i][1] == 0) or (pendant[i][0] == 0 and pendant[i][1] == 1):
            print(i ,' ')
    print(' ')

# dt du
def isComplete():
    d = degree_OfUnDirected()
    n = len(getList())

    for i in range(len(d)):
        if d[i][0] != n - 1:
            return False
    return True

def toUndirected():
    matrix = getList()
    n = len(matrix)

    d = np.empty(shape=(n,n), dtype = int)
    d.fill(0)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                d[i][j] = d[j][i] = 1

    return d

def complement():
    matrix = getList()
    n = len(matrix)

    comp = np.empty(shape=(n,n), dtype = int)
    comp.fill(0)

    for i in range(n):
        for j in range(n):
            if i != j:
                if matrix[i][j] == 1:
                    comp[i][j] = 0
                else:
                    comp[i][j] = 1
    return comp

def matrix_to_list():
    graph = {}
    matrix = getList()
    for i, node in enumerate(matrix):
        adj = []
        for j, connected in enumerate(node):
            if connected:
                adj.append(j)
        graph[i] = adj
    return graph

def BFS(begin):
    graph = matrix_to_list()
    visited = [False] * (len(getList()))
    queue = []
    queue.append(begin)
    visited[begin] = True

    while queue:
        begin = queue.pop(0)
        print(begin, end = ' ')
        for i in graph[begin]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True

def DFS(begin, visited, result):
    visited[begin] = True
    
    result.append(begin)
    matrix = getList()

    for i in range(len(matrix)):
        if matrix[begin][i] == 1 and not visited[i]:
            DFS(i, visited, result)

def isPath(a, b):
    result = []
    visited = [False] * (len(getList()))
    DFS(a, visited, result)
    for i in range(len(result)):
        if b == result[i]:
            return True
    return False

def DFS_traverse(begin, visited):
    visited[begin] = True
    matrix = toUndirected()

    for i in range(len(matrix)):
        if matrix[begin][i] == 1 and not visited[i]:
            DFS_traverse(i, visited)

def isConnected():
    for i in range (len(getList())):
        visited = [False] * (len(getList()))
        DFS_traverse(i, visited)
        for j in range (len(getList())):
            if not visited[j]:
                return False
    return True

def Euler():
    d = degree_OfUnDirected()
    matrix = getList()
    n = len(matrix)
    odd = 0

    if not isConnected():
        print(' not Eulerian')
    else:
        for i in range(n):
            if d[i][0] % 2 != 0:
                odd+=1
        if odd == 0:
            print(' is Eulerian')
        elif odd == 2:
            print(' is not Eulerian path')
        elif odd > 2:
            print('is not Eulerian')

def isBipartite():
    a = getList()
    n = len(a)
    if isUndirected():
        G = nx.from_numpy_matrix(a, create_using=nx.Graph())
    else:
        G = nx.from_numpy_matrix(a, create_using=nx.DiGraph())

    if (nx.is_bipartite(G)):
        return True
    else:
        return False

def isCompleteBipartite():
    if isBipartite() & isComplete():
        return True
    return False

def cutVertex():
    G = nx.from_numpy_matrix(getList())
    return list(nx.articulation_points(G))

def bridgeEdges():
    G = nx.from_numpy_matrix(getList())
    return list(nx.bridges(G))



def main():
    getMatrix()
    print(getList())
    print(' undirected graph ?: ',isUndirected())
    print('Number of Vertexs: ', num_OfVertex())
    print('Number of edges: ', num_OfEdges())
    if isUndirected() == True:
        degree_OfUnDirected()
    else:
        print(degree_OfDirected())

    print('Isolated vertices: ', isIsolated())
    print('Pendant vertices: ')
    isPendant()
    print('Is complete graph: ?', isComplete())
    print('Directed to Undirected: ')
    print(toUndirected())
    print('To complement: ')
    print(complement())
    print('BFS:')
    BFS(1)
    list = []
    visited = [False] * (len(getList()))
    print('\nDFS')
    DFS(1, visited, list )
    print(list)
    print(isPath(2, 4))
    print('Graph is connected: ', isConnected())
    Euler()
    print('Is bipartite graph: ', isBipartite())
    print('Is complete bipartite graph: ', isCompleteBipartite())
    print('Cut vertices: ', cutVertex())
    print('Bridges edges: ', bridgeEdges())

if __name__ == '__main__':
    main()