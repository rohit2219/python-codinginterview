#https://leetcode.com/problems/alien-dictionary/

# The basic idea here is to create graphs using each poistion of the word and do a toplogical sort using them.
from collections import OrderedDict
def topoSort(graph,passVisited):

    visited=passVisited
    stack=[]
    if len(graph) < 1:
        return
    items = list(graph.items())
    start=items[0][0]
    stack.append(start)
    print('start',start)
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            visited.append(vertex)
        if vertex in graph:
            setchild=set(list(graph[vertex]))
        else:
            setchild=set()
        print('toposort:',vertex,setchild,visited)

        for curVertex in setchild -set(visited):
            if curVertex not in visited:
                visited.append(curVertex)
            stack.append(curVertex)
    return visited

def alienDict(inpList):
    graphList=[]
    maxlen=0
    for i in inpList:
        if len(i) > maxlen:
            maxlen=len(i)
    ctrletter=0
    invalidOrderFlag=False
    print('maxlen',maxlen)
    try:
        for k in range(maxlen):
            graphWord=OrderedDict()
            for i in range(len(inpList)-1):
                #print('inpList:',inpList[k],k)
                if k > len(inpList[i]) - 1 or k > len(inpList[i + 1]) - 1:
                    break
                #print('next and prev word',inpList[i], inpList[i + 1])
                if inpList[i][k] != inpList[i+1][k]:
                    if inpList[i][k] in graphWord or inpList[i+1][k] in graphWord:
                        invalidOrderFlag=True
                        break
                    else:
                        #print('adding:',inpList[i][k])
                        graphWord[inpList[i][k]]=inpList[i+1][k]

                if invalidOrderFlag is True:
                    break
            graphList.append(graphWord)
    except IndexError:
        print('indexerr',i,k)
    if invalidOrderFlag is True:
        return ''
    print('graphList######:',graphList)
    visit=[]
    for graph in graphList:
        retVisit=topoSort(graph,visit)
        print(visit)
        visit=retVisit
    return

inpList=[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
alienDict(inpList)
