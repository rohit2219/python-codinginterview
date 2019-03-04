import copy
class Node():
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None
class LRUCache():
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.dict = {}
        self.capacity = capacity
        self.lenCache = 0

    def add(self, inpNode):
        # add to a doubly linked list, adding to head
        if self.head is None:
            inpNode.next=None
            inpNode.prev=None
            #print('addInpNode:',inpNode,inpNode.next,inpNode.prev)
            self.head=inpNode
            #print('addhead:',self.head,self.head.next,self.head.prev)
            self.tail=self.head
            #print('addtail:', self.tail, self.tail.next, self.tail.prev)
            self.tail.next=None
            self.lenCache = self.lenCache + 1
            return
        inpNode.next = self.head
        inpNode.prev = None
        self.head.prev = inpNode
        self.head = inpNode
        self.head.prev=None
        self.lenCache = self.lenCache + 1
        return
    def remove(self, curNodeToDel):
        print('removal',curNodeToDel,curNodeToDel.next)
        # prev nodes next becomes curNodes next and not to curNode
        if curNodeToDel.next != None:
            curNodeToDel.prev.next = curNodeToDel.next
            curNodeToDel.next.prev = curNodeToDel.prev
        else:
            curNodeToDel.prev.next = None
            self.tail = curNodeToDel.prev
            self.tail.next=None
        self.lenCache = self.lenCache - 1
        return
    def put(self, key, val):
        if key in self.dict:
            self.remove(self.dict[key])
        newNode = Node(key, val)
        self.add(newNode)
        self.dict[key] = newNode
        if self.lenCache > self.capacity:
            tailKey = self.tail.key
            self.remove(self.tail)
            del self.dict[tailKey]
        #print('afterput:','head:',self.head,self.head.next,self.head.prev, 'tail:',self.tail,self.tail.next,self.tail.prev)
        #print(self.dict)
        print('put lencache', self.lenCache,key)
        return
    def get(self,key):
        if key not in self.dict:
            return -1
        nodeToGet = self.dict[key]
        self.remove(nodeToGet)
        print(self.lenCache)
        #print('afterremove',self.head.key, self.tail.key)
        self.add(nodeToGet)
        #print('afteradd',self.head.key, self.tail.key)
        self.dict[key] = self.head
        #print(self.head.key,self.tail.key,self.dict)
        print('get lencache',self.lenCache,key)
        return self.head.value

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # returns 1
cache.put(3, 3)
print(cache.get(2))       # returns -1 (not found)
