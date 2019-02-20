#Inorder means it displays it in the ascending order ie lesser to greater, so we travel like left subtree, node, rigthsbtree
#PREORDER traversal pretty much means that displaying tree in the way its supposd to be displayed, ie start from top node and move down Node left and then right
#POSTORDER means we display the child node first and then move up to the parent..So left subtree first, right subtree and node

class Node(object):
    def __init__(self, val):
        self.data = val
        self.rchild = None
        self.lchild = None

    def setRight(self, x):
        self.rchild = x

    def setLeft(self, x):
        self.lchild = x

class binTree(object):
    def __init__(self, x):
        ## create the rootNode while instantiating the Binary tree
        self.rootNode = Node(x)
        self.rootNode.rchild = None
        self.rootNode.lchild  = None
    def inorder(self,travelnode):
        if travelnode == None:
            return
        self.inorder(travelnode.lchild)
        print("Node:",travelnode.data)
        self.inorder(travelnode.rchild)

    def postorder(self,travelnode):
        if travelnode == None:
            return
        self.postorder(travelnode.lchild)
        self.postorder(travelnode.rchild)
        print("Node:",travelnode.data)

    def preorder(self,travelnode):
        if travelnode == None:
            return
        print("Node:",travelnode.data)
        self.preorder(travelnode.lchild)
        self.preorder(travelnode.rchild)


    def find(self ,x):
        findFlag = False
        curNode = self.rootNode
        if curNode.data == x: return True
        ## This would go on infinite loop In case of corner cases
        print(findFlag,curNode.lchild,curNode.rchild )
        while ( findFlag == False ) and ( ( curNode.lchild != None ) and ( curNode.rchild != None ) ) :
            print("start:",curNode.data)

            if   x < curNode.data :
                curNode = curNode.lchild
                print('find## moving to left:')
            else:
                curNode = curNode.rchild
                print('find## moving to left:')
            print("end:", curNode.data,curNode,curNode.lchild,curNode.rchild)
            if curNode != None :
                if curNode.data == x:
                    print("found")
                    findFlag = True
                    return findFlag

        return

    def insertNode(self, x):
        curNode = self.rootNode
        ## This would go on infinite loop if same value is added
        while (True):
            print("curNode:",curNode.data,curNode.rchild,curNode.lchild)
            if x < curNode.data:
   #             curNode = curNode.lchild
                print('moving to left:')
                if curNode.lchild != None :
                    curNode = curNode.lchild
                else:
                    curNode.lchild = Node(x)
                    print('inserted :', x)
                    break
            else:
                print('moving to right:')
   #             curNode = curNode.rchild
                if curNode.rchild != None:
                    curNode = curNode.rchild
                else:
                    curNode.rchild = Node(x)
                    print('inserted:', x)
                    break
        return
    def binTreeReversal(self):
        if self.isSymmetric(self.rootNode):
            self.reverseTree(self.rootNode)
        else:
            print('Not symmetric')
            return None
        return
    def isSymmetric(self,passNode):
        if passNode==None:
            return
        if passNode.rchild == None and passNode.lchild == None:
            return True
        if passNode.rchild == None or passNode.lchild == None:
            return False

        return self.isSymmetric(passNode.lchild) and self.isSymmetric(passNode.rchild)

    def reverseTree(self,passRoot):
        # swap nodes
        if passRoot == None:
            return
        tempNode = Node(passRoot.data)
        tempNode=passRoot.rchild
        passRoot.rchild=passRoot.lchild
        passRoot.lchild=tempNode
        self.reverseTree(passRoot.rchild)
        self.reverseTree(passRoot.lchild)

        return

    '''
    Binary Tree reversal - try this
isSymmetric

isSymmetricHelper(root.left,root.right)


isSymmetricHelper(node1,node2){

	if node1 == None and node2 == None
		return true
	if node1 == None or node2 == None
		return false
	return isSymmetricHelper(node1.left,node1.right) &&
	isSymmetricHelper(node2.left,node2.right)
	
}

def reverseBin(root):
	if root == None:
		return
	temp = Node(root.right)
	root.right=root.left
	root.left=temp
	reverseBin(root.left)
	reverseBin(root.right)

if issymmetric(root) == True:
	reverseBin(root)
else:
	return None    
    '''
if __name__ == "__main__":
#    node=Node(3)
#    print(node.data,node.lchild,node.rchild)
#    exit()
    btree=binTree(5)
    #val = [3, 9, 4, 1, 7, 30]
    '''
    simple bin tree
      5
    3   9
    '''

    val = [3,9]
    for i in val:
        btree.insertNode(i)
    print("##################################")
    #btree.find(30)
    #print("Found element Find:-",btree.find(9))
    #print("POSTORDER ##################################")

    #print(btree.postorder(btree.rootNode))

    #print("INORDER ##################################")

    #print(btree.inorder(btree.rootNode))
    print("PREORDER ##################################")

    print(btree.preorder(btree.rootNode))
    print('##Reversing && preorder')
    btree.binTreeReversal()
    print(btree.preorder(btree.rootNode))
