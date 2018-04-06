# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-05 18:09:08
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:28:33

# Program to Reverse a string using Stack


class Solution():
    def createStack(self):
        stack = []
        return stack

    # Function to check if a stack is empty
    def isEmpty(self, stack):
        return len(stack) == 0

    # Function to push an element to stack
    def push(self, stack, data):
        stack.append(data)
        print "data pushed to stack : ", data

    # Function to pop an element from stack
    def pop(self, stack):
        if self.isEmpty(stack):
            print "stack empty, cannot pop"
            return -1
        else:
            print "element popped : ", stack[-1]
            return stack.pop()

    def reverseString(self, str1):
        stk = self.createStack()
        res = ""
        for i in range(0, len(str1)):
            self.push(stk, str1[i])

        for i in range(0, len(str1)):
            res = res + self.pop(stk)

        return res


# create an object of a class Solution
obj = Solution()

# the input string
str1 = 'Awasthi'

result = obj.reverseString(str1)

print "Input string : ", str1
print "The reversed string is : ", result
