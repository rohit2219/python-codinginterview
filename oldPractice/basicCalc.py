#https://leetcode.com/problems/basic-calculator-ii/
def calculate(str):
    stack=[]
    oper="+"
    num=0
    for i in range(len(str)):
        print(str[i])
        if str[i].isdigit():
            num=int(str[i])
        if str[i] in ["+","-","/","*"]:
            if oper == "+":
                stack.append(num)
            elif oper == "-":
                stack.append(num * -1)
            elif oper == "/":
                stack.append(int(stack.pop() / num))
            elif oper == "*":
                stack.append(int(stack.pop() * num))
            oper=str[i]
            num = 0
    print(stack)
    return sum(stack)
print(calculate("2-1/2*4+3"))