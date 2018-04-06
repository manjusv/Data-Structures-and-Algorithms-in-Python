# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-15 15:32:59
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:19:47


class Node():
    # create a Node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution():
    # Function to do level oder traversal of a binary tree
    def LevelOrderTraversal(self, root):

        # create a empty queue
        queue = []
        # insert root to queue
        queue.insert(0, root)
        while len(queue) > 0:
            # pop the node at front from queue
            temp = queue.pop()
            # print the node
            print temp.val,

            # insert the left node to queue if left node exists
            if temp.left is not None:
                queue.insert(0, temp.left)
            # insert the right node to queue if right node exists
            if temp.right is not None:
                queue.insert(0, temp.right)


# create an obj of the class
obj = Solution()

# create a tree to do level order traversal
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print "level Order Traversal of the binary Tree : ", obj.LevelOrderTraversal(root)
