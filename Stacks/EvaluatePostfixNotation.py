# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-06 15:20:00
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-06 17:24:36

# Python program to evaluate value of a postfix expression

class Solution:
	def isOperator(self, op):
		if op in '+-*/':
			return True
		return False

	def isEmpty(self, stack):
		return len(stack) == 0

	def FindRes(self, op1, op2, op):
		if op == '+':
			return op1 + op2
		if op == '-':
			return op1 - op2
		if op == '*':
			return op1 * op2
		if op == '/':
			# take care of -ve values
			if op1 * op2 < 0 and op1 % op2 != 0:
				return (op1/op2+1)
			return op1 / op2

	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
		stack = []
		for item in A:
			if self.isOperator(item) is False:
				stack.append(item)
			else:
				op2 = int(stack.pop())
				op1 = int(stack.pop())
				res = self.FindRes(op1, op2, item)
				stack.append(res)
			
		return stack.pop()

# create an object of a class
obj = Solution()

exp = ["4","-2","/","2","-3","-","-"]

print "The result after evaluation of postfix notation : ", obj.evalRPN(exp)