# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-13 17:20:41
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-13 18:07:41

# Program to find the duplicate element in a given array, if multiple duplicates then return any one

class Solution:
    # @param A : list of integers
    # @return an integer
    def repeatedNumber(self, A):
        # iterate over the list one by one
        for i in range(0, len(A)):
            # check for sign of elements
            if A[abs(A[i])] >= 0:
                # make it negative
                A[abs(A[i])] = -A[abs(A[i])]
            else:
                # if this is the first duplicate, return
                return abs(A[i])

# create an obj of the class
obj = Solution()

# Input the list of integers
A = [1, 2, 1, 4, 3, 4, 5]

print "The any one duplicate element in given list : ", obj.repeatedNumber(A)