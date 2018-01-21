# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-22 00:40:03
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-22 01:06:26

# Given a BST node, return the node which has value just greater than the given node.
# If there are no successor in the tree, return NULL

class Node():
    # create a Node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution:
    # Function to get inorder traversal of BST
    def inorderTraversal(self, root):
        # create an empty stack
        stack = []
        
        # result to return
        result = []
        
        # assign the root to cur
        cur = root
        
        while True:
            if cur is not None:
                # push node to stack
                stack.append(cur)
                cur = cur.left
                
            else:
                if len(stack) > 0:
                    # pop a node from stack
                    popped_node = stack.pop()
                    result.append(popped_node)
                    
                    cur = popped_node.right
                else:
                    break
        
        return result
        
    # @param A : root node of tree
    # @param x : integer
    # @return the root node in the tree
    def getSuccessor(self, root, x):
        # Inorder traversal of BST gives a sorted array
        inorder_traversal = self.inorderTraversal(root)
        # Find x in inorder traversal and return next element if it exists
        n = len(inorder_traversal)
        for i in range(0, n - 1):
            if inorder_traversal[i].val == x and i < (n - 1):
                return inorder_traversal[i + 1].val
        return None

# create an object of the class
obj = Solution()

# create a BST
root = Node(6)
root.left = Node(4)
root.right = Node(7)
root.left.left = Node(3)
root.left.right = Node(5)

x = input("Enter the value of x : ")

print "The next greater element : ", obj.getSuccessor(root, x)