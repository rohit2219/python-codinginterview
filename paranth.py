
def isMatchParan(paranStr):

    paranMap={
        ']':'[',
        ')': '(',
        '}': '{',
    }
    stack=[]
    unmatchFlag=True
    for i in paranStr:
        #print('stack:',stack,'i:',i)
        if i in paranMap.values():
            stack.append(i)
            print('append:',i)
        elif stack == [] or stack.pop() != paranMap[i]:
                print('unmatched in ',i)
                unmatchFlag=False
                break
    if unmatchFlag:
        if stack==[]:
            unmatchFlag=True
        else:
            unmatchFlag=False

    return unmatchFlag

#print(isMatchParan('[()]'))

def insertComma(numStr):
    outStr=''
    ctr=1
    for i in reversed(numStr):
        print(ctr,i)
        if ctr %3 == 0:
            outStr=','+ i +outStr
        else:
            outStr=i+outStr
        ctr+=1

    return outStr



print(insertComma('1234'))
lcaVal=0
def postOrder(root,n1,n2,n1Found,n2Found,lcaFound):
    if root == None or lcaFound:
        return
    if  n1Found == False and n1==root:
        n2Found=True
    if n2Found == False and n1==root:
        n2Found=True

    postOrder(root.left,n1,n2,n1Found,n2Found)
    postOrder(root.right,n1,n2,n1Found,n2Found)
    if n2Found and n1Found:
        lcaVal=root
        lcaFound=True

    return lca
def lca(root,n1,n2):

    lca=postOrder(root,n1,n2,False,False,False)
    return

