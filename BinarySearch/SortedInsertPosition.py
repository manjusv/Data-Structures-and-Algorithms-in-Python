# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-21 01:30:41
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-21 02:15:49

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

class Solution:
	# Function to get Insert index or index at which element is found
    def getInsertIndex(self, A, low, high, x):
        while low <= high:
            mid = low + (high - low) / 2
            if x == A[mid]:
                return mid
            elif x < A[mid]:
                high = mid - 1
            elif x > A[mid]:
                low = mid + 1
        return low
            
    # @param A : list of integers
    # @param x : integer
    # @return an integer
    def searchInsert(self, A, x):
        low = 0
        high = len(A) - 1
        return self.getInsertIndex(A, low, high, x)
		
# create an object of the class
obj = Solution()

# Take input from user
n = input("Enter how many elements in array : ")
print "Enter elements of array : "
for i range(0, n):
	A.append(input())
	
x = input("Enter value of x : ")
print "The index(found or to be inserted at) of given element in A : ", obj.searchInsert(A, x)