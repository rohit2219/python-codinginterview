#https://leetcode.com/problems/group-anagrams/

class solution(object):

    def groupAnagrams(self,inpList):
        memoDict={}
        outList=[]
        for word in inpList:
            sortedWord = ''.join(sorted(word))
            if sortedWord in memoDict:
                posOfWord=memoDict[sortedWord]
                outList[posOfWord].append(word)
            else:
                memoDict[sortedWord] = len(outList)
                outList.append([word])

