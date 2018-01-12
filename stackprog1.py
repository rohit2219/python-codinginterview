import sys

class MinStack(object):
    def __init__(self):
        self.myList = []
        self.minmyList = None
        self.maxmyList = None
    def push(self, x):
        self.minmyList=self.getMin()
        if self.minmyList == None or x < self.minmyList :
            self.minmyList=x
        self.myList.append((x,self.minmyList))
        return None

    def pop(self):
        itemToPop = self.myList[len(self.myList) - 1]
        self.myList.pop()
        return None


    def top(self):
        if len(self.myList) > 0:
            return self.myList[len(self.myList) - 1][0]
        else:
            return None

    def getMin(self):
        if len(self.myList) > 0:
            return self.myList[len(self.myList) - 1][1]
        else:
            return None
obj = MinStack()


##["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
##[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)
print("curlist:",obj.myList)
print("top printed",obj.top())
obj.pop()
obj.getMin()
obj.pop()
print("curlist:",obj.myList)
print(obj.getMin())
obj.pop()
obj.push(2147483647)
obj.top()
obj.getMin()
obj.push(-2147483648)
obj.top()
obj.getMin()
obj.pop()
print(obj.getMin())
exit()


obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.myList)
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())
exit()

obj.push(2147483647)
obj.top()
obj.getMin()


obj.pop()
obj.getMin()
print("curlist:",obj.myList)
obj.pop()

param_3 = obj.top()
print("curlist:",obj.myList)

exit()

obj.push(0)
obj.push(1)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())

exit()
param_3 = obj.top()
param_4 = obj.getMin()
#testList = MinStack()
#testList.push(-2)
#testList.push(0)
#testList.push(-3)

#print(testList.myList)
#print("min value ", testList.getMin())
#testList.pop()
#print ("list after pop", testList.myList)
