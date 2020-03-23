#https://leetcode.com/problems/word-search/

def createGraph(matrix):
    graph = {}
    rowLen=len(matrix)
    colLen=len(matrix[0])
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            child=set()
            if (row + 1 < rowLen):
                graph[(row,col)] = child.add((row+1,col))
            if (row - 1 > 0):
                graph[(row,col)] = child.add((row-1,col))
            if (col + 1 < colLen):
                graph[(row,col)] = child.add((row,col + 1))
            if (col - 1 > 0):
                graph[(row,col)] = child.add((row,col -1))
            graph[(row,col)] = child
    return graph


def pathToString(path, matrix):
    string=""
    for i in path:
        #print("i:",i[0],i[1])
        #print("matrix:",matrix)
        string=string+matrix[i[0]][i[1]]
    return string

class Solution:
    def exist(self, board, word: str) -> bool:
        #create the graph DS
        graphMat = createGraph(board)
        # do a DFS with path
        start=(0,0)
        visited=set()
        stack=[(start,[start])]
        for i in graphMat:
            print(i,":",graphMat[i])
        while stack:
            vertex,path=stack.pop()
            #visited.append(vertex)
            for curVertex in graphMat[vertex] - set(path):
                #visited.add(curVertex)
                print('curVertex:',curVertex)
                stack.append((curVertex,path + [curVertex]))
                # see if the path is same as string if yes retunr true else return fals
                print('path:',path + [curVertex],pathToString(path + [curVertex],board))
                if pathToString(path + [curVertex],board) == word:
                    return True


        return False


input = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
x=Solution()
print(x.exist(input,"ABCCED"))
