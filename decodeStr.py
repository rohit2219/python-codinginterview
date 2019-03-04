#https://leetcode.com/problems/decode-string/

def decodeStr(inpStr):

    for i in range(len(inpStr)):
        stack=[]
        cc=''
        cd=0
        outStr=''
        if inpStr[i] == '[':
            stack.append(cd)
            stack.append(cc)
            cc=''
            cd=0
        elif inpStr[i] == ']':
            prevStr=stack.pop()
            cd=stack.pop()
            cc=prevStr+cc*cd
        elif type(inpStr[i]) is str :
            cc=cc+inpStr[i]
        elif type(inpStr[i]) is int :
            cd=int(inpStr[i])

    return cc

print(decodeStr('3[a]2[bc]'))