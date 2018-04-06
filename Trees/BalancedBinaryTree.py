# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-17 01:10:33
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:32:50

# Progrm to check if the given binary tree is height balanced or not


class Node():
    # create a Node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    # Function to find maxdepth of a node
    def maxDepth(self, root):
        if root is None:
            return 0
        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1

    # @param root : root node of tree
    # @return an integer
    def isBalanced(self, root):
        if root is None:
            return True
        # for a tree to be balanced the left and right subtrees should also be balanced
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False


# create an obj of the class
obj = Solution()

# create a tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)
root.left.left.left.left = Node(8)

if obj.isBalanced(root):
    print "Tree is height balanced"
else:
    print "The tree is not height balanced"
