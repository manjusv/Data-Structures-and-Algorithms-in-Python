# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-07 16:34:34
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:28:23

# Program to validate if the input string has redundant braces


class Solution:
    def isEmpty(self, stack):
        return len(stack) == 0

    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []

        for i in range(0, len(A)):
            # push to stack till a ')' is encountered
            if A[i] != ')':
                stack.append(A[i])
            else:
                count = 0
                # count no of chars between '(' and ')' braces
                while self.isEmpty(stack) is False and stack[-1] != '(':
                    stack.pop()
                    count = count + 1

                if count < 2:
                    return True
                # uncomment below lines if you dont want to consider ending braces as valid ones
                # if i == len(A) - 1 and self.isEmpty(stack) is False:
                #   return True
                stack.pop()
        return False


# create an object of the class
obj = Solution()

input_string = "()"

if obj.braces(input_string):
    print "Redundant Braces"
else:
    print "No Redundant Braces"
