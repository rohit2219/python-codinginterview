def findWater1(arr, n):
    # initialize output
    result = 0

    # maximum element on left and right
    left_max = 0
    right_max = 0

    # indices to traverse the array
    lo = 0
    hi = n - 1
    i=0
    while (lo <= hi):
        i=i+1
        if (arr[lo] < arr[hi]):

            if (arr[lo] > left_max):

                # update max in left
                left_max = arr[lo]
            else:

                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo += 1

        else:

            if (arr[hi] > right_max):
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi -= 1

    return result


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
def rainWater(inpArr,lenArr):
    rMaxArr=[]
    lMaxArr=[]
    water=0
    # find max traversing through the right
    rMaxArr = [0 for i in range(lenArr)]
    lMaxArr = [0 for i in range(lenArr)]

    rMaxArr[lenArr-1]=inpArr[lenArr-1]
    for i in reversed(range(lenArr-1)):
        if inpArr[i] > rMaxArr[i+1]:
            rMaxArr[i]=inpArr[i]
        else:
            rMaxArr[i] = rMaxArr[i + 1]
    print(rMaxArr)
    # find maxx traversing thru left
    lMaxArr[0]=inpArr[0]
    for i in range(1,lenArr):
        if inpArr[i] > lMaxArr[i-1]:
            lMaxArr[i]=inpArr[i]
        else:
            lMaxArr[i]=lMaxArr[i-1]
    print(lMaxArr)

    #traverse thru array and see the water content in each node
    for i in range(lenArr):
        water=water+min(rMaxArr[i],lMaxArr[i])-inpArr[i]

    return water

#print("Maximum water that can be accumulated is ",rainWater(arr, n))
marks=[['A',10],['B',20],['C',20],['X',40],['A',30],['B',70],['C',10],['B',60],['B',20]]
def maxAvg(inpArr):
    #1) tot of marks how many subjects, maxAvg
    subjMap={}
    avgMap={}
    maxAvg=inpArr[0][1]

    for i in range(len(inpArr)):
        if inpArr[i][0] in subjMap:
            subjMap[inpArr[i][0]]=subjMap[inpArr[i][0]] + 1
            avgMap[inpArr[i][0]]= ( avgMap[inpArr[i][0]] + inpArr[i][1] ) / subjMap[inpArr[i][0]]
            if avgMap[inpArr[i][0]] > maxAvg:
                maxAvg=avgMap[inpArr[i][0]]
                personMaxAvg=inpArr[i][0]
        else:
            subjMap[inpArr[i][0]] = 1
            avgMap[inpArr[i][0]]=inpArr[i][1]
    return personMaxAvg
#print(maxAvg(marks))

def robPos(inpStr):

    posMap={
        'U':['y',1],
        'D':['y',-1],
        'R':['x',1],
        'L':['x',-1]
    }
    #####x,y
    pos=[0,0]
    for i in inpStr:
        if posMap[i][0] == 'x':
            pos[0]=pos[0] + posMap[i][1]
        else:
            pos[1] = pos[1] + posMap[i][1]
    return pos

#print(robPos('RUUD'))

def revStr(inpStr):
    #if len(inpStr) == 0:
    #    return
    #print(inpStr[-1:])
    #return revStr(inpStr[:-1])
    for i in range(len(inpStr)):
        print(inpStr[len(inpStr) - 1 -i])
    return
#revStr('AABB')

def maxpaths(m,n):
    if m == 1 or n==1:
        return 1
    else:
        return maxpaths(m-1,n) + maxpaths(m,n-1)

#print(maxpaths(2,2))

def maxSteps(totSteps):

    first=1
    second=2
    totCombos=0
    for i in range(totSteps-2):
        totCombos=first+second
        first=second
        second=totCombos
    return totCombos
#print(maxSteps(4))

def DynamicProgrammingSingleSellProfit(arr):
    # If the array is empty, we cannot make a profit.
    if len(arr) == 0:
        return 0

    # Otherwise, keep track of the best possible profit and the lowest value
    # seen so far.
    profit = 0
    cheapest = arr[0]
    prevProfit=0
    prevCheap=arr[0]
    currCheapPos=0
    currProfitPos=0
    prevCheapPos=0
    prevProfitPos=0
    # Iterate across the array, updating our answer as we go according to the
    # above pseudocode.
    for i in range(1, len(arr)):
        # Update the minimum value to be the lower of the existing minimum and
        # the new minimum.
        cheapest = min(cheapest, arr[i])
        if (prevCheap != cheapest):
            prevCheapPos=currCheapPos
            currCheapPos=i
        # Update the maximum profit to be the larger of the old profit and the
        # profit made by buying at the lowest value and selling at the current
        # price.
        print(i,cheapest)
        profit = max(profit, arr[i] - cheapest)
        if profit!=prevProfit:
                prevProfitPos=currProfitPos
                currProfitPos=i
        prevProfit=profit
        prevCheap=cheapest
    return [prevCheapPos,currProfitPos,profit]

arr=[5,10,7,14,4,5]
print(DynamicProgrammingSingleSellProfit(arr))

[5,10,10,14,14,14,14]
[5,5,5,5,4,4]
def maxProfit(inpArr):
    cheapest = inpArr[0]
    maxProfit = 0
    cheapPos=0

    for i in range(1, len(inpArr)):
        if inpArr[i] < cheapest:
            cheapest=inpArr[i]
        profit=max(profit,inpArr[i]-cheapest)
    return profit