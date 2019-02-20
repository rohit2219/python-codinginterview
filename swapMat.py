# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
def swapArr(arr1, arr2):
    return arr2, arr1


def swapRows(inpMat):
    swapCnt = 0
    if len(inpMat) % 2 == 0:
        swapCnt = len(inpMat) / 2
    else:
        swapCnt = int(len(inpMat) / 2)
    for i in range(swapCnt):
        inpMat[i], inpMat[len(inpMat) - 1 - i] = swapArr(inpMat[i], inpMat[ len(inpMat) - 1 - i] )
    return inpMat


def transPoseSwap(inpMat):
    for i in range(len(inpMat)):
        for j in range(len(inpMat[0])):
            if i != j and j > i:
                inpMat[i][j], inpMat[j][i] = inpMat[j][i],inpMat[i][j]
    return inpMat


def rotate(matrix):
	return transPoseSwap(swapRows(matrix))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#print(rotate(matrix))


def thirdMax(inpArr):
    maxArr = []

    for i in inpArr:
        maxArr.append(i)
        maxArr.sort()
        if len(maxArr) > 3:
            maxArr = maxArr[0:3]
    print(maxArr)
    return maxArr[2]
print(thirdMax([2,3,6,5,4,1]))