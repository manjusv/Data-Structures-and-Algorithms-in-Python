# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-04 18:34:26
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:17:33

# Program to count occurances of an element in a sorted list


class Solution:
    def LastOccurance(self, A, low, high, x):
        if high >= low:
            mid = (low + high) // 2
            if (A[mid] == x) and (mid == len(A) - 1 or x < A[mid + 1]):
                return mid
            elif x < A[mid]:
                # go to right half of array
                return self.LastOccurance(A, low, mid - 1, x)
            else:
                return self.LastOccurance(A, mid + 1, high, x)
        return -1

    def FirstOccurance(self, A, low, high, x):
        if high >= low:
            mid = (low + high) // 2
            if (A[mid] == x) and (mid == 0 or x > A[mid - 1]):
                return mid
            elif x > A[mid]:
                # go to right half of array
                return self.FirstOccurance(A, mid + 1, high, x)
            else:
                return self.FirstOccurance(A, low, mid - 1, x)
        return -1

    # Function to count occurance of element x in array A
    def findCount(self, A, x):
        # find index of first occurance of element x
        i = self.FirstOccurance(A, 0, len(A) - 1, x)

        # find the last occurance of element x
        j = self.LastOccurance(A, i, len(A) - 1, x)

        if i == -1 or j == -1:
            return 0
        # the no of occurances will be
        return j - i + 1


# create an obj of class
obj = Solution()
A = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10]
x = 1
print "Element {0} occurs {1} times".format(x, obj.findCount(A, x))
