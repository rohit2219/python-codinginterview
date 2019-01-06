
def swapFn(a,b):
    return b,a

class matrix:
    def __init__(self,x = []):
        self.inpMat = x
    def tranMat(self):
        for x in range(len(self.inpMat)):
            if len(self.inpMat) != len(self.inpMat[x]):
                print('returning')
                return
        maxLen=len(self.inpMat)
        print(maxLen)
        for i in range(len(self.inpMat)):
            for j in range(len(self.inpMat[i])):
                if i == j:
                    break;
                print(i,j,maxLen-i,maxLen-j)
                print('swapping',self.inpMat[i][j], self.inpMat[maxLen-i][maxLen-j])
                self.inpMat[i][j], self.inpMat[maxLen-i][maxLen-j]=swapFn(self.inpMat[i][j], self.inpMat[maxLen-i][maxLen-j])
        print(self.inpMat)

m = matrix([[4,4,4,3],
            [4,4,3,5],
            [4,3,5,5],
            [3,5,5,5]]
           )
#m=matrix([[1,2,3],[4,5,6],[7,8,9]])
m.tranMat()
