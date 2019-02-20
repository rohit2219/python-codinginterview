class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            print('i:',i)
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

                maxStr=s[start:i+1]
                print(maxStr,i,start+1)
                print(usedChar)
            usedChar[s[i]] = i

        return maxLength

    def rohitFunction(self,str):
        start=maxLen=longStr=0
        usedMap={}
        for i in range(len(str)):

           if str[i] in usedMap and usedMap[str[i]] >= start :
                start=usedMap[str[i]]+1
           else:
               maxLen=max(maxLen,(i+1)-start)
               print(start, i + 1,maxLen)
               maxStr=str[start:(i+1)]
               print(maxStr,maxLen)
           usedMap[str[i]] = i
        return maxLen
x = Solution()
print(x.rohitFunction('aabccaefghde'))

def reArrZer(self,inpArr):

    for i in range(len(inpArr)):
        if inpArr[i] == 0:
            inpArr=inpArr[0:i] + inpArr[i+1:len(inpArr)]
            inpArr.append(0)
    return inpArr
def validBraces(self,inpStr):
    braceMap={
        '}':'{',
        ']':'[',
        ')':'('
    }
    stack=[]
    for i in inpStr:
        if i in braceMap.values():
            stack.append(i)
            print(i,' appended')
        elif i in braceMap.keys():
            print(i, 'in keys',braceMap[i])
            if stack == [] or braceMap[i] != stack.pop():
                return False
    return True
def validBraces(self,inpStr):
    braceMap={
        '}':'{',
        ']':'[',
        ')':'('
    }
    stack=[]
    for i in inpStr:
        if i in braceMap.values():
            stack.append(i)
            print(i,' appended')
        elif i in braceMap.keys():
            print(i, 'in keys',braceMap[i])
            if stack == [] or braceMap[i] != stack.pop():
                return False
    return True

#print(x.reArrZer([0,1,2,3,0,4,5,0]))
#print(x.validBraces('[{()}]())'))
import collections
import heapq
import functools

def topKFrequent(words, k):
    counts = collections.Counter(words)
    print(counts,type(counts),counts.items())

    items = list(counts.items())
    print(items)
    items.sort(key=lambda tup:tup[1])
    print('after sort',items)
    #items.sort(key=lambda item: (-item[1], item[0]))
    return [item[0] for item in items[0:k]]


#print(topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 3))




