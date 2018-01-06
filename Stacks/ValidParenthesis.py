# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-06 12:30:53
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-06 13:08:02

# Program to check if the string contains valid set of brackets

class Solution:
    # check if opening and closing characters match
    def isMatch(self, X, Y):
        if X == '{' and Y == '}':
            return True
        elif X == '[' and Y == ']':
            return True
        elif X == '(' and Y == ')':
            return True
        else:
            return False

    # pop an element from stack
    def pop(self, stack):
        del stack[-1]
    
    # check if the stack is empty
    def isEmpty(self, stack):
        return len(stack) == 0
        
    # @param A : string
    # @return True or False
    def isValid(self, A):
        stack = []
        
        # push all the items to the stack
        for i in range(0, len(A)):
            # push to stack if it is opening item
            if A[i] == '{' or A[i] == '[' or A[i] == '(':
                stack.append(A[i])

            # check if char is closing item
            elif A[i] == '}' or A[i] == ']' or A[i] == ')':
                # if closing item is the first char, return False
                if len(stack) == 0:
                    return False
                # check if it is not matching with top of stack
                if self.isMatch(stack[-1], A[i]) is False:
                    return False
                # once there is a match, pop an elemnt from stack
                self.pop(stack)
        
        # check if stack is empty, if yes return True
        if self.isEmpty(stack):
            return True
        return False

# create an object of the class
obj = Solution()

input_string = '{}()[][]()'

if obj.isValid(input_string):
    print "It is Valid"
else:
    print "Not Valid"