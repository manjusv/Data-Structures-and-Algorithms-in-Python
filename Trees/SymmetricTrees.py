# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-15 20:18:47
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-15 20:51:40

class Node():
	# create a Node
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Solution:
	# take mirror tree of same tree
    def _isSymmetric(self, root1, root2):
    	# if empty trees, then symmetric
        if root1 is None and root2 is None:
            return True
        # if left subtree of tree1 is symmetric with right subtree of tree2
        if root1 is not None and root2 is not None and root1.val == root2.val and self._isSymmetric(root1.left, root2.right) and self._isSymmetric(root1.right,root2.left):
            return True
        return False

    # @param root : root node of tree
    # @return an integer
    def isSymmetric(self, root):
        return self._isSymmetric(root, root)

# create an obj of class
obj = Solution()

# create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(2)

if obj.isSymmetric(root):
	print "The trees are Symmetric"
else:
	print "The trees are not Symmetric"