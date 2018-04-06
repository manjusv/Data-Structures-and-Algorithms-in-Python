# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-04 17:37:40
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:17:54


class Solution:
    def _findMin(self, A, low, high):
        # if no rotation at all return first element
        if A[high] > A[low]:
            return A[0]

        # if there is only one element in array
        if low == high:
            return A[low]

        mid = int((low + high) / 2)

        # check if mid + 1 is the smallest
        if mid < high and A[mid + 1] < A[mid]:
            return A[mid + 1]
        # check is mid is the smallest
        if mid > low and A[mid] < A[mid - 1]:
            return A[mid]

        # go either left half or right half
        if A[mid] < A[high]:
            return self._findMin(A, low, mid - 1)
        return self._findMin(A, mid + 1, high)

    # Function to find min element in sorted rotated array
    def findMin(self, A):
        low = 0
        high = len(A) - 1
        return self._findMin(A, low, high)


# create an object of class
obj = Solution()
A = [6, 7, 8, 0, 1, 2]
min_ele = obj.findMin(A)

print "Min Element in array : ", min_ele
