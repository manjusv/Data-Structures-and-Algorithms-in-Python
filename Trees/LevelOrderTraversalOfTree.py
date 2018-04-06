# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-15 14:40:41
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:33:27


class Node():
    # create a Node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution():
    # Function to calculate the height of the tree
    def height(self, root):
        if root is None:
            return 0
        else:
            # calculate the height of left subtree
            lheight = self.height(root.left)
            # # calculate the height of right subtree
            rheight = self.height(root.right)

            # return max height of left and right subtree
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    # Function to print all nodes in a given level
    def printGivenLevel(self, root, level):
        if root is None:
            return
        # if level is 1 print the only element
        elif level == 1:
            print root.val,
        # traverse left and right subtree if level > 1 and decrement level by 1
        elif level > 1:
            self.printGivenLevel(root.left, level - 1)
            self.printGivenLevel(root.right, level - 1)

    def LevelOrderTraversal(self, root):
        # determine the height of the tree
        h = self.height(root)
        # call printGivenLevel for every level
        for d in range(1, h + 1):
            self.printGivenLevel(root, d)


# create an obj of the class
obj = Solution()

# create a tree to do level order traversal
root = Node(1)
root.left = Node(12)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print "level Order Traversal of the binary Tree : ", obj.LevelOrderTraversal(root)
