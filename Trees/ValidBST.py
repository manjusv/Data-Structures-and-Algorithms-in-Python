# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-21 22:41:11
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-21 23:16:13

# Given a binary tree, determine if it is a valid binary search tree (BST).

import sys

class Node():
	# create a Node
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Solution:
    def _isValidBST(self, root, MIN, MAX):
        if root is None:
            return 1
        if root.val < MIN or root.val > MAX:
            return 0
        return self._isValidBST(root.left, MIN, root.val - 1) and self._isValidBST(root.right, root.val + 1, MAX)
        
    # @param root : root node of tree
    # @return an integer
    def isValidBST(self, root):
    	# for a BST root value > max(left subtree) and root value < min(right subtree)
        return self._isValidBST(root, -sys.maxint - 1, sys.maxint)

# create an obj of the class
obj = Solution()

# create a binary tree
root = Node(6)
root.left = Node(4)
root.right = Node(7)
root.left.left = Node(3)
root.left.right = Node(5)


if obj.isValidBST(root):
	print "Valid BST"
else:
	print "Not a Valid BST"