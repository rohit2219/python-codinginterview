
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def bfsShortpath(graph):

    queue=[]
    start='A'
    queue.append((start,[start]))
    visited=set()
    dest='D'
    shortPath=['A' for i in range(10)]
    while queue:
        vertex,path=queue.pop(0)
        visited.add(vertex)
        for curVertex in graph[vertex] - set(path):
            print('graphvertex and path:',graph[vertex] , set(path))
            print(curVertex,path)
            visited.add(curVertex)
            queue.append((curVertex, path + [curVertex]))
            if curVertex == dest and len(path + [curVertex]) < len(shortPath):
                shortPath=path + [curVertex]
    print('shortPath',shortPath)
    return

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
#bfsShortpath(graph)
'''
Non cyclic graph flow
     -->B   -->D
A-->X-->C-->-->E
 -->Y       -->F
'''

nonCyclicgraph = {'A': set(['X', 'Y']),
         'X': set(['C', 'B']),
         'C': set(['D', 'E','F']),
        'B':set(['P','Q'])
                  }
nonCyclicgraph={
    'B':set(['A']),
    'C': set(['A']),
    'X': set(['B']),
    'Y': set(['B','K'])
}
def dfsTopo(start):
    visitedOrder=[]
    stack=[start]

    while stack:
        vertex=stack.pop()
        if vertex not in visitedOrder:
            visitedOrder.append(vertex)
        if vertex in nonCyclicgraph:
            children=nonCyclicgraph[vertex]
        else:
            children=set()
        for childVertex in children - set(visitedOrder):
            if childVertex not in visitedOrder:
                visitedOrder.append(childVertex)
            stack.append(childVertex)
    print(visitedOrder)
    return

#dfsTopo('B')


def dfsShortpath(graph):

    stack=[]
    start='A'
    visited=set()
    path=[]
    stack.append((start,path))
    pathsToDest=[]
    dest='D'
    while stack:
        vertex,path=stack.pop()
        visited.add(vertex)
        for childvertex in graph[vertex] - set(path):
            stack.append((childvertex,[vertex]+path))
            visited.add(childvertex)
            if childvertex == 'D':
                pathsToDest.append([vertex]+path)
    print(pathsToDest)
    return

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
dfsShortpath(graph)
