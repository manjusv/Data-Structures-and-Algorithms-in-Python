# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-10 19:20:55
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:35:44

# Program to remove all instances of an element from array, return number of elements left in the array


class Solution:
    # @param A : list of integers
    # @param val : integer
    # @return an integer
    def removeElement(self, A, val):
        # two pointers i and j from start and end
        i = 0
        j = len(A) - 1
        while i <= j:
            # when i and j point to same element
            if i == j and A[i] == val:
                del A[i]
                j -= 1
            # when both elements pointed by i and j are equal to val
            elif A[i] == val and A[j] == val:
                del A[i]
                j -= 1
                del A[j]
                j -= 1
            # when only element pointed by i is equal to val
            elif A[i] == val:
                del A[i]
                j -= 1
            # when only element pointed by j is equal to val
            elif A[j] == val:
                del A[j]
                j -= 1
            else:
                i += 1
                j -= 1
        # return the list after all instances of element are removed
        return A


# create an obj of the class
obj = Solution()

A = [1, 3, 4, 5, 1, 3, 4, 5, 9, 2, 4]
val = 1

print "Input list : ", A
A = obj.removeElement(A, val)

print "The array after the element is removed : ", A
print "Length after removing all instances of element : ", len(A)
