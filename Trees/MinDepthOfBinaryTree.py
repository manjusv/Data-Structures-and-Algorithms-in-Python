# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-15 19:10:19
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:34:04


class Node():
    # create a Node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    # @param root : root node of tree
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        # if left subtree is null then return min from right subtree
        if root.left is None:
            return self.minDepth(root.right) + 1
        # if right subtree is null then return min from left subtree
        if root.right is None:
            return self.minDepth(root.left) + 1

        # if left and right subtrees are not null then return min of both subtrees
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# create an obj of the class
obj = Solution()

# create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(6)

print "The min Depth of the binary Tree : ", obj.minDepth(root)
