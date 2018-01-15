# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-15 17:01:46
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-15 17:37:02

class Node():
	# create a Node
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Solution:
    # @param root : root node of tree
    # @return a list of integers
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

# create an object of a class
obj = Solution()

# create a tree to do inorder traversal
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print "The inorder Traversal of the given Binary Tree : ", obj.inorderTraversal(root)