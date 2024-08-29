
def simWord(list1,list2,pairList):
# same number of words
    simWordFlag=True
    if len(list1) != len(list2):
        simWordFlag = False
        return simWordFlag
    wordMap={}
#transitive similar
    for i in len(range(pairList)):
        if pairList[i][0] in wordMap:
            wordMap[pairList[i][0]].append(pairList[i][1])
        else:
            # symmetric similar
            wordMap[pairList[i][0]] = [pairList[i][1]]
            if wordMap[pairList[i][1]] in wordMap:
                wordMap[pairList[i][1]].append([pairList[i][0]])
            else:
                wordMap[pairList[i][1]] = pairList[i][0]
    stack=[]
    visited={}
    for word in wordMap:
        stack.append(word)
        while stack:
            vertex=stack.pop()
            visited.append(vertex)
            for i in set(wordMap[word]) - visited:
                if i in wordMap:
                    wordMap[word].append(wordMap[i])
                    stack.append(i)
    ctr=0
    while ctr < len(list):
        if list1[ctr] in wordMap[list1[ctr]]:
            continue
        else:
            simWordFlag=False
            break

        ctr+=1

    return simWordFlag