#https://leetcode.com/problems/decode-string/

def decodeStr(s):
    stack = []; curNum = 0; curString = ''
    for c in s:
        if c == '[':
            stack.append(curString)
            stack.append(curNum)
            curString = ''
            curNum = 0
        elif c == ']':
            print('at ]:',stack)
            num = stack.pop()
            prevString = stack.pop()
            curString = prevString + num*curString
        elif c.isdigit():
            #curNum = curNum*10 + int(c)
            curNum =  int(c)
        else:
            print('char:',c,curString)
            curString = curString + c
    return curString

#print(decodeStr('3[a]2[bc]'))
print(decodeStr("2[abc]3[cd]ef"))