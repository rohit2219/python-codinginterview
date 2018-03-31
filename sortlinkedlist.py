
class Node(object):
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode
    def getData(self):
        return self.data
    def addData(self,val):
        self.data = val
    def setNext(self,val):
        self.nextNode = val

class linList(object):
    def __init__(self,head = None):
        self.head = head
        self.size = 0
    def 