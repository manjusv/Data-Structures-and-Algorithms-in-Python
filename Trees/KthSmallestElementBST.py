# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-16 00:10:52
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:33:16

# Program to find kth smallest element from a Binary Search Tree( BST )


class Node():
    # create a Node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    # Indrder traversal of a BST gives sorted array as output
    def inorderTraversal(self, root):
        # create an empty stack
        stack = []

        # result to return
        result = []

        # assign the root to cur
        cur = root

        while True:
            if cur is not None:
                # push node to stack
                stack.append(cur)
                cur = cur.left

            else:
                if len(stack) > 0:
                    # pop a node from stack
                    popped_node = stack.pop()
                    result.append(popped_node.val)

                    cur = popped_node.right
                else:
                    break

        return result

    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    def kthsmallest(self, root, k):
        # call inorder traversal of BST to get sorted array
        sorted_array = self.inorderTraversal(root)

        # Now kth smallest element will be sorted_array[k - 1]
        return int(sorted_array[k - 1])


# create an object of a class
obj = Solution()

# create a BST
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(6)

k = input("Enter Value of k : ")
print "The kth smallest element in the given Binary Search Tree : ", obj.kthsmallest(root, k)
