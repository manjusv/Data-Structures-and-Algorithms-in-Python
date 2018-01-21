# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-21 20:40:27
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-21 21:04:09

# Program to search for a value in an m x n matrix.

class Solution:
    # @param A : list of list of integers
    # @param x : integer
    # @return an integer
    def searchMatrix(self, A, x):
    	# since each row is sorted use binary search for each row
        for i in range(0, len(A)):
            low = 0
            high = len(A[i]) - 1
            while low <= high:
            	# find mid
                mid = low + (high - low) / 2
                if x == A[i][mid]:
                    return True
                elif x < A[i][mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False

# create an obj of class
obj = Solution()

# Take input from user
m = input("Enter no of rows in matrix : ")
n = input("Enter no of columns in matrix : ")

M = []

print "Enter the elements : "
for i in range(0, m):
	s = []
	for j in range(0, n):
		s.append(input())
	M.append(s)

x = input("Enter the element to search : ")

if obj.searchMatrix(M, x):
	print "Element found"
else:
	print "Element not found"

