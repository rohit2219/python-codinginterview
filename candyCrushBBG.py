def candyCrush(str):
    print('input',str)
    start=0
    end=0
    outStr=[]
    for i in range(len(str)):
        if i > 0 and str[i]!=str[i-1]:
            start=i-1
        end=i
        outStr.append(str[i])
        if end-start > 3:
            toPop=end-start
            while toPop > 0:
                outStr.pop()
                toPop-=1
            candyCrush(''.join.outStr + str[end:])
    return ''.join(outStr)
print(candyCrush('AACBBCCCBBDD'))























'''    for i in range(len(str)):
    if i > 1 and str[i]  != str[i-1]:
        if end-start >= 3:
            popCount=end-start
            print('before popo:',outStr,start,end)
            while popCount > 0:
                outStr.pop()
                popCount=popCount-1
            print('after popo:',outStr,str[end:len(str)])
            print('return:',''.join(outStr)+str[end:len(str)])
            return candyCrush(''.join(outStr)+str[end:len(str)])
            start=i-1
    outStr.append(str[i])
    end=i
return ''.join(outStr)

'''
