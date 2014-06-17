
import sys
import os

class node:
    ''' stores integral entries in binary search tree '''
    def __init__ (self, num):
        self.rightNode = None
        self.leftNode = None
        self.data = num

class binarySearchTree:
    ''' Binary search tree implementation'''
    def __init__ (self, num):
        self.root = node(num)

    def insertNode (self, parNode, num):
        if parNode != None:
            print parNode.data
            if num < parNode.data :
                if parNode.leftNode == None:
                    parNode.leftNode = node(num)
                else:
                    self.insertNode(parNode.leftNode, num)
            else:
                if parNode.rightNode == None:
                    parNode.rightNode = node(num)
                else :
                    self.insertNode(parNode.rightNode, num)
        return

    def printInorder (self, node):
        '''Inorder display of Binary Search tree '''
        if node.leftNode != None:
            self.printInorder (node.leftNode)
        print str(node.data)
        if node.rightNode != None:
            self.printInorder (node.rightNode)

tree = binarySearchTree(20)
tree.insertNode (tree.root, 15)
tree.insertNode (tree.root, 25)
tree.insertNode (tree.root, 35)

print "Inorder : "
tree.printInorder(tree.root)

'''
print "Testing :"
print "Root : " + str(tree.root.data)
print "Left :" + str(tree.root.leftNode.data)
print "Right : " + str(tree.root.rightNode.data)
'''
