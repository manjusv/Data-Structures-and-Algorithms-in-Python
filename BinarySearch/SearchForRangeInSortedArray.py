# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-21 01:10:41
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-02-08 17:35:35

# Given a sorted array of integers, find the starting and ending position of a given target value.

class Solution:
	# Function to get the starting index of element x in array A
    def getStartIndex(self, A, low, high, x):
        if low <= high:
            mid = low + (high - low) / 2
            if x < A[mid]:
                return self.getStartIndex(A, low, mid - 1, x)
            elif x > A[mid]:
                return self.getStartIndex(A, mid + 1, high, x)
            elif x == A[mid]:
                if mid == 0 or (mid > 0 and x != A[mid - 1]):
                    return mid
                else:
                    return self.getStartIndex(A, low, mid - 1, x)
            else:
                return -1
        return -1
            
	# Function to get ending index of element x in array A
    def getEndIndex(self, A, low, high, x):
        if low <= high:
            mid = low + (high - low) / 2
            if x < A[mid]:
                return self.getEndIndex(A, low, mid - 1, x)
            elif x > A[mid]:
                return self.getEndIndex(A, mid + 1, high, x)
            elif x == A[mid]:
                if mid == high or (mid < high and x != A[mid + 1]):
                    return mid
                else:
                    return self.getEndIndex(A, mid + 1, high, x)
            else:
                return -1
        return -1
            
                
    # @param A : tuple of integers
    # @param x : integer
    # @return a list of integers
    def searchRange(self, A, x):
        low = 0
        high = len(A) - 1
        first = self.getStartIndex(A, low, high, x)
        last = self.getEndIndex(A, low, high, x)
        return [first, last]
		
# create an object of class
obj = Solution()

# Take input from user
A = []
n = input("Enter how many elements in array : ")
print "Enter elements of array : "
for i in range(0, n):
	A.append(input())
	
x = input("Enter value of x : ")
print "The starting and Ending index of given element in A : ", obj.searchRange(A, x)