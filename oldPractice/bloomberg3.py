import copy


class Node():
    def __init__(self, inpToNode):
        self.data = inpToNode
        self.next = None
        self.random = None


class linList():
    def __init__(self):
        self.head = None

    def insertNode(self, inpData):
        if self.head == None:
            tempNode = Node(inpData)
            self.head = tempNode
            self.head.next = None
        else:
            tempNode = Node(inpData)
            tempNode.next = self.head
            self.head = tempNode

    def travelList(self):
        curNode = self.head
        while curNode != None:
            print('list data:', curNode.data)
            curNode = curNode.next

    def reverseList(self):
        print('revresal linked list')
        prevNode = None
        curNode = self.head
        nextNode = self.head.next
        print(curNode.data, nextNode.data, prevNode)
        i = 0
        while curNode != None:
            curNode.next = prevNode
            tempNode = nextNode
            self.head = curNode
            prevNode = curNode
            if nextNode != None:
                nextNode = nextNode.next
            curNode = tempNode
        return

    def insertNodeObj(self, inpNode):
        inpNode.next = self.head
        self.head = inpNode
        return

    def copyLinList(self):
        copyListObj=linList()
        curNode = self.head
        copyNode = copy.copy(self.head)
        print(copyNode,self.head)
        copyListObj.head = copyNode
        copyListObj.head.next=None
        print('########')
        copyListObj.travelList()
        print('########')

        while curNode is not None:
            curNode = curNode.next

            if curNode is None:
                break;
            print('curNode:',curNode.data)
            copyNode = copy.copy(curNode)
            copyListObj.insertNodeObj(copyNode)
        return copyListObj


def addLinLists(head1, head2):
    curNode1 = head1
    curNode2 = head2
    resList = linList()
    carryDigit = 0
    sumDigit = 0
    while curNode1 != None or curNode2 != None:
        sumDigit = curNode1.data + curNode2.data + carryDigit
        if sumDigit > 10:
            sumDigit = sumDigit % 10
            carryDigit = 1
        else:
            carryDigit = 0
        resList.insertNode(sumDigit)
    if carryDigit != 0:
        resList.insertNode(1)

    return


# h
# 1>>2>>3
# p<<c

# list1=linList()
##This is 32
# list1.insertNode(2)
# list1.insertNode(3)
# list1.travelList()

##This is 45
list2 = linList()
list2.insertNode(5)
list2.insertNode(4)
list2.travelList()
# time.sleep(5)
#list2.reverseList()
# list2.travelList()
list2Copy=list2.copyLinList()
list2Copy.travelList()