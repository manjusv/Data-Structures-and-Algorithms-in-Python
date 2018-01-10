# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-10 17:36:06
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-10 17:47:37

# Program to find the length of last word in a given string

class Solution():
	# Function to find length of last word
	def LenOfLastWord(self, A):
		# start from end of string
		i = len(A) - 1

		# Initialize count to 0
		count = 0

		# skip all the blank spaces at end
		while(i >= 0 and A[i] == ' '):
			i -= 1

		# check if there were no words
		if i < 0:
			return 0
		else:
			while( i >= 0 and A[i] != ' '):
				count += 1
				i -= 1
			return count

# create an object of class
obj = Solution()

# take input from user
s = raw_input("Enter the input string : ")

print "length of last word in given string : ", obj.LenOfLastWord(s)