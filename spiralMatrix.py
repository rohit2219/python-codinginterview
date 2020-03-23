
00 01 02
10 11 12
20 21 22

def toggleRowTravel(curDir):
    if curDir=='R':
        return "L"
    else:
        return 'R'

def toggleColTravel(curDir):
    if curDir=='U':
        return "D"
    else:
        return 'U'

def toggleTravel(rowOrCol):
    if rowOrCol=='RO':
        return "CO"
    else:
        return 'CO'


def spiralMat(matArr):
    finArr=[]
    colLenMat=len(matArr[0])
    rowLenMat=len(matArr)
    maxRow=rowLenMat
    maxCol=colLenMat
    curRowDir='R' #R,L
    curColDir='D' #D U
    curTravel='RO' #RO CO
    curPos=(0,0)
    rightTopPt=(0,colLenMat-1)
    leftTopPt=(0,0)
    leftBottomPt=(rowLenMat-1,0)
    rightBottomPt=(rowLenMat-1,colLenMat-1)

    while True:
        if curTravel=='RO' and curRowDir =='R':
            i,j=curPos[0],curPos[1]
            while j < rightTopPt[1]:
                j+=1
                curPos=(i,j)
                finArr.append(matArr[i][j])
            #toggle
            #update rightTopPt
        elif curTravel=='RO' and curColDir =='L':
            i,j=curPos[0],curPos[1]
            while j > leftBottomPt[1]:
                j-=1
                curPos=(i,j)
                finArr.append(matArr[i][j])
            #Toggle
            #update leftBottomPt
        elif curTravel=='CO' and curColDir =='D':
            i,j=curPos[0],curPos[1]
            while i < rightBottomPt[0]:
                i+=1
                curPos=(i,j)
                finArr.append(matArr[i][j])
            #Toggle
            #update rightBottomPt

        elif curTravel=='CO' and curRowDir =='U':
            i,j=curPos[0],curPos[1]
            while i >= leftTopPt[0]:
                i-=1
                curPos=(i,j)
                finArr.append(matArr[i][j])
            #Toggle
            #update leftTopPt

            if len(finArr) == colLenMat*rowLenMat
                break
    return finArr

matArr=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(spiralMat(matArr))