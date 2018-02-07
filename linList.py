## Code to set node
class node(object):
    def __init__(self, inpData=None, nextNode=None):
        self.data = inpData
        self.next = nextNode

    def getData(self):
        return self.data

    def setData(self, x):
        self.data = x

    def getNext(self):
        return self.next

    def setNext(self, n):
        self.next = n


## Code for Lined List ops

class linList(object):
    def __init__(self, headData):
        self.head = node(headData)
        self.tail = node(headData)

    def insertNode(self, x ):
        newNode = node(x)
        newNode.setNext(self.head)
        self.head = newNode

    def delNode(self, d):
        curNode = self.head
        prevNode = self.head
        while (curNode != None):
            if (curNode.getData() == d ):
                prevNode.next = curNode.getNext()

            #print(curNode.data)
            prevNode = curNode
            curNode = curNode.getNext()

    def viewLinList(self):
        curNode = self.head
        count = 0
        while (curNode != None):
            count = count + 1
            print(curNode.data)
            curNode = curNode.getNext()


obj = linList(4)
obj.insertNode(5)
obj.insertNode(6)
obj.insertNode(7)
obj.insertNode(10)

obj.viewLinList()
print("tail:",obj.tail.data, "head:",obj.head.data)

obj.delNode(6)

obj.viewLinList()
print("tail:",obj.tail.data, "head:",obj.head.data)

print('hello complete')
