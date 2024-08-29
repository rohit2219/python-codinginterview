#https://leetcode.com/problems/valid-square/
import math
def sideLen(ptArr):
    x1=ptArr[0][0]
    y1=ptArr[0][1]
    x2=ptArr[1][0]
    y2=ptArr[1][1]
    return math.sqrt((x2-x1)^2+(y2-y1)^2)

def isValidSq4Pts(p1,p2,p3,p4):
    #) compose different sides of a square
    sArr=[[p1,p2],[p2,p3],[p3,p4],[p4,p1]]

    # Find length of each side of a square, if they are all equal 1st cond pass.
    if ( (sideLen(sArr[0]) == sideLen(sArr[1])) == (sideLen(sArr[2]) == sideLen(sArr[3])) ):
        firstCond=True
    else:
        firstCond=False

    # if dist between diagonal points is ^2 times any side, then 1nd cond pass
    if ( (sideLen(sArr[0]) * math.sqrt(1/2)) == sideLen([p2,p3])):
        secCond=True
    else:
        secCond=False

    # if first cond and 2nd cond, return true else false
    return firstCond or secCond

p1 p2
p3 p4