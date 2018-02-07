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
            end = mid
        else:
            print('searching right of mid')
            start = mid


li = [1,3,4,9,11,12]
findIt = 11

print(binSrch(li,findIt))
