# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-15 17:00:58
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-15 18:14:33

class Node():
	# create a Node
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Solution:
    # @param root : root node of tree
    # @return a list of integers
    def postorderTraversal(self, root):
        # create a empty stack
        stack = []
        
        # result contains the reverse of postorder traversal
        result = []
        
        # push root to stack1
        stack.append(root)
        while len(stack) > 0:
            # pop a node from stack1
            popped_node = stack.pop()
            result.append(popped_node.val)
            
            if popped_node.left is not None:
                stack.append(popped_node.left)
            if popped_node.right is not None:
                stack.append(popped_node.right)
                
        return result[::-1]

# create an object of a class
obj = Solution()

# create a tree to do inorder traversal
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print "The postorder Traversal of the given Binary Tree : ", obj.postorderTraversal(root)