def binSrch(arrList, item):
    start = 0
    end = len(arrList) - 1
    foundFlag = False


    while ( start <= end ) and (foundFlag == False):

        mid = int((start + end) / 2)
        if arrList[mid] == item:
            foundFlag = True
            return (foundFlag,mid)
            break
        print("start:",mid, start, end, item)
        if (arrList[mid] > item):
            print('searching left of mid')
            end = mid - 1
        else:
            print('searching right of mid')
            start = mid + 1
    return (False,None)


li = [1,3,4,9,11,12]
findIt = 1

print(binSrch(li,findIt))
