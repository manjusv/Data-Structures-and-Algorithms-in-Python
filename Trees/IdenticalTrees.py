# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-15 19:40:35
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-15 20:11:23

class Node():
	# create a Node
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Solution:
    # @param root1 : root node of tree1
    # @param rppt2 : root node of tree2
    # @return an integer
    def isSameTree(self, root1, root2):
    	# if both trees are empty
        if root1 is None and root2 is None:
            return 1
        # if one tree is empty and other not empty
        elif root1 is not None and root2 is None:
            return 0
        elif root1 is None and root2 is not None:
            return 0
        # if both trees are not empty and corresponding nodes match return True
        elif (root1.val == root2.val) and self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right):
            return 1
        return 0

# create an obj of class
obj = Solution()

# create a binary tree1
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

# create a binary tree2
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

if obj.isSameTree(root1, root2):
	print "The trees are identical"
else:
	print "The trees are not identical"