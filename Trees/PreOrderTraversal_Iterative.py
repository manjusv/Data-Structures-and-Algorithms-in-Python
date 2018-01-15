# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-15 16:05:56
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-15 16:50:44

# Program to print PreOrder Traversal of a Tree without using Recursion

class Node():
	# create a Node
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Solution:
    # @param root : root node of tree
    # @return a list of integers
    def preorderTraversal(self, root):
        # result to return
        result = []
        
        # create an empty stack
        stack = []
        
        # push the root to stack
        stack.append(root)
        
        while len(stack) > 0:
            # pop an item from stack and print it
            temp = stack.pop()
            result.append(temp.val)
            
            # push right child of popped node
            if temp.right is not None:
                stack.append(temp.right)
            # push left child of popped node
            if temp.left is not None:
                stack.append(temp.left)
                
        return result

# create an object of a class
obj = Solution()

# create a tree to do level order traversal
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print "The preorder Traversal of the given Binary Tree : ", obj.preorderTraversal(root)