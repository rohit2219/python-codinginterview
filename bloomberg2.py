def isomorphic(str1, str2):
    # error handling

    # pre map between strings of 1 &2
    mapStr = {}
    isIsomorphic = True
    for i in range(len(str1)):
        if (str1[i] in mapStr) and (mapStr[str1[i]] != str2[i]):
            isIsomorphic = False
            break
        mapStr[str1[i]] = str2[i]
    # replace str1 using the map and see if its equal to str2

    return isIsomorphic
#print(isomorphic('foo','tee'))


def strRemove(inpStr,remChar):
        outStr=''
        countMap={}
        maxCount=3
        notExceedMapCount=False
        if remChar is not None:
            for i in inpStr:
                if i not in remChar:
                    outStr=outStr+i
            return strRemove(outStr,None)
        else:
            for i in inpStr:
                if i in countMap:
                    countMap[i]=countMap[i]+1
                else:
                    countMap[i]=1
                print(i)
                if countMap[i] >= maxCount:
                    print('recursion:',inpStr,i)
                    return strRemove(inpStr,i)
                outStr=outStr+i
        return outStr

#print(strRemove('ABCCCCBBA',None))


def compareSwap(tup1, tup2):
    if tup1[0] > tup2[0]:
        return tup1, tup2
    else:
        return tup2, tup1


def sortCharCount(inpStr):
    countMap = {}
    for i in inpStr:
        if i in countMap:
            countMap[i] = countMap[i] + 1
        else:
            countMap[i] = 1

    listChar = []
    for i in countMap:
        tempTup = (i, countMap[i])
        listChar.append(tempTup)
    listChar.sort(key=lambda x: x[1])
    outChar = ''

    for i in range(len(listChar)):
        if i + 1 < len(listChar) - 1 and  listChar[i][1] == listChar[i + 1][1]:
            listChar[i], listChar[i + 1] = compareSwap(listChar[i], listChar[i + 1])
            for j in range(listChar[i][1]):
                outChar = outChar + listChar[i][0]
        else:
            for j in range(listChar[i][1]):
                outChar = outChar + listChar[i][0]
    return outChar
#print(sortCharCount('aabbccceddd'))

def add2Sum(inpArr,sumNum):
    sorted(inpArr)
    print(inpArr)
    l=0
    r=len(inpArr)-1
    outList=[]
    count=0
    while l<r:
        #print(l,r)
        if inpArr[l] + inpArr[r] == sumNum:
            outList.append([inpArr[l],inpArr[r]])
            l=l+1
        elif inpArr[l] + inpArr[r] < sumNum:
            l=l+1
        else:
            r=r-1

    print('finalop',outList)
    return outList
#add2Sum([1,2,3,4,5],7)

[1,2,3,4,5],8

def addmainSum(inpList,target):
    outList=[]
    inpList.sort()
    for i in range(len(inpList)):
        listRet=add2Sum(inpList[i:len(inpList)], target-inpList[i])
        print('listRest',listRet)
        for eachList in listRet:
            eachList.append(inpList[i])
            outList.append(eachList)
    print('outList',outList)
    return outList
#addmainSum([1,2,3,4,5],8)


def word_break_recursive(given_string, dictionary):
    """"Returns None if the given string cannot be broken into words, otherwise returns space separate words."""

    given_string_length = len(given_string)
    if given_string_length == 0:
        return ""
    string = ""
    for i in range(given_string_length):
        string += given_string[i]
        print('string',string)
        if string in dictionary:
            print('reccall:',given_string[i + 1:])
            r = word_break_recursive(given_string[i + 1:], dictionary)
            if r is not False:
                string += " " + r
                return string
    return False

print(word_break_recursive("hellohowar",['hello',"how","are","you"]))
