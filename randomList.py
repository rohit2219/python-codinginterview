# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
# heads
# a -> b -> c ->d
# a -b & a->None
import copy


class Solution(object):
    #def copyRandomList(self, head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    self.visitedHash = {}

    def checkNode(self,nodePointer):
        if nodePointer in self.visitedHash:
            return nodePointer[nodePointer]
        else:
            if nodePointer == None:
                return None
            clonePointer = RandomListNode(nodePointer.label)
            self.visitedHash[nodePointer] = clonePointer
            return clonePointer

    def copyRandomList(self, head):
        curNode = head
        newNodeHead = None
        while curNode != None:
            if curNode in self.visitedHash:
                self.visitedHash[curNode].next = self.visitedHash[curNode.next]
                self.visitedHash[curNode].random = self.visitedHash[curNode.random]
            else
                cloneHead = RandomListNode(curNode.label)
                self.visitedHash[curNode] = cloneHead
                if curNode == self.head:
                    newNodeHead = cloneHead
                cloneHead.next = self.checkNode(curNode.next)
                cloneHead.random = self.checkNode(curNode.random)
            curNode = curNode.next
        return None