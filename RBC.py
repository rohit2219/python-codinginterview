#https://leetcode.com/problems/missing-ranges/


'''
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''
def numBtw(a,b):
    if b-2 == a:
        return str(b-1)
    else:
        return str(a+1) + str(b-1)

def findMiss(inpArr,numMax,numMin):
    missArr=[]
    if inpArr[0] >= numMin:
        missArr.add(numBtw(numMin,inpArr[0]))

    for i in range(1,len(inpArr)):
        if inpArr[i - 1] + 1 == inpArr[i]:
            continue
        else:
            missArr.append(numBtw(inpArr[i - 1],inpArr[i]))

    if inpArr[-1] < numMax:
        missArr.append(inpArr[-1],numMax)
    return

