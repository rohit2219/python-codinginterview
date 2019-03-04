
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
bfs(graph)