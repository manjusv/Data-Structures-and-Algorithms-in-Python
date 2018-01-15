# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-15 18:35:31
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-15 19:25:05

class Node():
	# create a Node
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Solution:
    # @param root : root node of tree
    # @return an integer
    def maxDepth(self, root):
    	# return 0 if emtry tree
        if root is None:
            return 0
        # find max depth of left and right subtree
        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)
        
        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1

# create an obj of the class
obj = Solution()

# create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(6)

print "The max Depth of the binary Tree : ", obj.maxDepth(root)