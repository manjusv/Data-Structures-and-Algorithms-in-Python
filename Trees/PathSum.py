# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-16 00:50:09
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-16 01:21:03

# Program to find if there exists a path from root to leaf, such that sum of elements in path equals given sum

class Node():
	# create a Node
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return an integer
    def hasPathSum(self, root, sum1):
    	# if tree is empty and sum given is 0 then return true
        if root is None:
            if sum1 == 0:
                return True
        
        # Initialize result as True
        res = 0
        # calculate subsum
        subsum = sum1 - root.val
        # if leaf is reached and sum is equal then return True
        if subsum == 0 and root.left is None and root.right is None:
            return 1
        # traverse left and right until a path with sum is found
        if root.left is not None:
            res = res or self.hasPathSum(root.left, subsum)
        if root.right is not None:
            res = res or self.hasPathSum(root.right, subsum)
        
        return res

# create an obj of the class
obj = Solution()

# create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

sum1 = input("Enter the sum : ")

if obj.hasPathSum(root, sum1):
	print "There is a path with given sum"
else:
	print "There is no path with given sum"