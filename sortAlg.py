
def srtswap(a, b):
    return b, a

def mergeSortList(right, left):
    lenR = len(right)
    lenL = len(left)
    lower = min(lenR, lenL) - 1
    l = 0
    r = 0
    m = 0
    mergeList = []
    while (l <= lower and r <= lower):
        if right[r] == left[l]:
            mergeList.append(left[l])
            mergeList.append(right[r])

            r = r + 1;
            l = l + 1;
            m = m + 1

        elif right[r] > left[l]:
            mergeList.append(left[l])
            l = l + 1;
            m = m + 1

        else:
            mergeList.append(right[r])
            r = r + 1;
            m = m + 1

    while (l < lenL):
        mergeList.append(left[l])
        l = l + 1;
        m = m + 1

    while (r < lenR):
        mergeList.append(right[r])
        r = r + 1;
        m = m + 1
    print("input lists:",right, left)
    print("returning lists:",mergeList)
    return mergeList


def mergeSort(inList):
    n = len(inList)
    leftL = [];rightL = []
    if n < 2: return

    mid = int(n / 2)
    leftL=  inList[0:mid]
    rightL= inList[mid:n]
    print("splitlists:",leftL,rightL)
    mergeSort(leftL)
    mergeSort(rightL)
    retlist = mergeSortList(leftL, rightL)
    return retlist

##3 go thru the list twice ie in two loops , swap the elements which are lesser than each other
def bubbleSort(inList):
    print("unsorted:",inList)
    for i in range(len(inList) - 1):
        swapFlag = False
        for j in range(len(inList) - 1):
            if inList[j] > inList[j + 1]:
                print("swapping",inList[j] , inList[j + 1])

                inList[j], inList[j + 1] = srtswap(inList[j], inList[j + 1])
                swapFlag = True
## which means its a sorted array
        if swapFlag == False:
            break
    return inList


def insertionSort(inList):
    for i in range(1, len(inList)):
        ## ur assigning the rightmost element as hole
        hole = inList[i]
        j = i -1
        print("hole",hole)
        ## looping from leftmost elemnt and shifting elements right if its greater than hole
        while j >=0 and hole < inList[j]:
             inList[j+1] = inList[j]
             print("shifting",inList[j+1] ,inList[j])
             j = j -1
        ## so when an element is not greater than hole,ie the shifting stops, that is where the hole should be inserted
        inList[j + 1] = hole
        print("moving hole to inlist[j]", hole, inList[j])
    return inList
## 4 quicksort

def partition(inpList,start,end):
    tempPivot = inpList[start]
    i = start + 1
    for j in range(start+1,end):
        if (inpList[j] < tempPivot):
            inpList[j], inpList[i]=srtswap(inpList[j],inpList[i])
            i = i + 1
        j=j+1

        inpList[start], inpList[i]=srtswap(inpList[start],inpList[i])
    return i-1

def quickSortHelp(inpList,start,end):
    if start < end:
        pivot=partition(inpList,start,end)
        quickSortHelp(inpList,start,pivot-1)
        quickSortHelp(inpList, pivot,end)
    else:
        return

def quickSort(inList):
    quickSortHelp(inList,0,len(inList)-1)

## quicksort ends

unSortLst = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83]
unSortLst = [63, 25, 73, 1]
unSortLst = [25,63,1,73]
#unSortLst = [5,7,2,3]
print("unsorted list:",unSortLst)

#print(bubbleSort(unSortLst))

#print(insertionSort(unSortLst))
#merge sorted list works, tested it..
#left = [1,2,4,7]
#right =  [1,3,5]

right = [63, 25]
left = [1 , 73]
#left = [1,2,4,7]
#right =  [1,3,5]
#right = [25,63]
#left = [1,73]


#print(mergeSortList(left,right))
print(mergeSort(unSortLst))
