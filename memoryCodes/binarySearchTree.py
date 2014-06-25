
import sys
import os

#[TODO] Deletions for BST
#[TODO] Empty tree and reconstruction
#{TODO] Tree empty check on all operations
# TODO Traversals, preorder and post order

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
        if node == None:
            return
        if node.leftNode != None:
            self.printInorder (node.leftNode)
        print str(node.data)
        if node.rightNode != None:
            self.printInorder (node.rightNode)

    def searchElement (self, node, num):
        ''' Searches integer number in the BST '''
        if node.data == num:
            return (node, True)
        elif num < node.data :
            if node.leftNode == None:
                return (node, False)
            else:
                return self.searchElement (node.leftNode, num)
        else :
            if node.rightNode == None:
                return (node, False)
            else :
                return self.searchElement (node.rightNode, num)

    def detatchNode (self, node):
        if node == self.root:
            self.root = None
        else:
            parentNode = self.root
            while ( True ):
                print parentNode.data
                if node.data < parentNode.data:
                    if parentNode.leftNode is node:
                        print "FOUND"
                        break
                    else :
                        parentNode = parentNode.leftNode
                else :
                    if parentNode.rightNode is node:
                        print "FOUND"
                        break
                    else :
                        parentNode = parentNode.rightNode
            if parentNode.leftNode is node:
                parentNode.leftNode = None
            else:
                parentNode.rightNode = None

    def deleteElement (self, node):
        ''' deletes specific node of BST '''
        if node.leftNode == None and node.rightNode == None:
            print "Node being deleted is : " + str(node.data)
            #self.detatchNode (node)
        elif node.leftNode != None and node.rightNode != None:
            node.data = node.leftNode.data
            self.deleteElement (node.leftNode)
        else :
            if node.leftNode != None:
                node.data = node.leftNode.data
                self.deleteElement (node.leftNode)
            else:
                node.data = node.rightNode.data
                self.deleteElement (node.rightNode)

    def deleteElementWrap (self, num):
        ''' deletes a number from a BST '''
        node, isFound = self.searchElement (self.root, num)
        if isFound == True:
            self.deleteElement (node)
        else :
            print "Element not found, Can't delete"


def main():
    print "Enter\nCreate Tree (1) \nPrintInorder (2)\nInsert Element(3) \nSearch element (4)"+ \
            "\nDelete Element (5)"
    while (1) :
        case = int(raw_input("ENTER: "))
        if case == 1:
            num = int(raw_input ("Root : "))
            tree = binarySearchTree(num)
        elif case == 2:
            tree.printInorder (tree.root)
        elif case == 3:
            num = int(raw_input ("Enter num to insert : "))
            tree.insertNode (tree.root, num)
        elif case == 4:
            num = int(raw_input ("Enter num to find : "))
            node, isFound = tree.searchElement (tree.root, num)
            if isFound == True:
                print "FOUND"
            else:
                print "NOT Found"
        elif case == 5:
            num = int(raw_input ("Enter num to delete : "))
            tree.deleteElementWrap (num)

if __name__ == "__main__":
    main()

'''
tree = binarySearchTree(20)
tree.insertNode (tree.root, 15)
tree.insertNode (tree.root, 25)
tree.insertNode (tree.root, 35)

print "Inorder : "
tree.printInorder(tree.root)

print "Testing :"
print "Root : " + str(tree.root.data)
print "Left :" + str(tree.root.leftNode.data)
print "Right : " + str(tree.root.rightNode.data)
'''
