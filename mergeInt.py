def canBeMerged(intLess, intMore):
    if intMore[0] <= intLess[1] and intMore[0] > intLess[0]:
        return True
    else:
        return False


def mergeTwoInt(intLess, intMore):
    return [intLess[0],intMore[1]]


def mergeInt(inpInt):
    # bring the intervals in ascending order of starting numbers
    inpInt.sort(key=lambda x: x[0])
    outInt = []

    if canBeMerged(inpInt[0], inpInt[1]):
        outInt.append(mergeTwoInt(inpInt[0], inpInt[1]))
    else:
        outInt.append(inpInt[0])
    print('before last loop',outInt)
    for i in range(1,len(inpInt)):
        print('inside last loop', outInt[len(outInt) - 1],inpInt[i],'--',outInt)
        if canBeMerged(outInt[len(outInt) - 1], inpInt[i]):
            temp=mergeTwoInt(outInt[len(outInt) - 1], inpInt[i])
            outInt.pop()
            outInt.append(temp)
        else:
            outInt.append(inpInt[i])

    return outInt

print(mergeInt([[1,2],[3,5],[5,7],[8,10],[13,15],[15,18]]))