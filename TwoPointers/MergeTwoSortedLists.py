# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-13 16:10:00
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-13 17:05:14

# Program to Merge Two given sorted Lists, the result should be in first list A

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        i = j = 0
        n = len(B)
        # since length of A changes, compare i with len(A)
        while i < len(A) and j < n:
            if A[i] == B[j]:
                A.insert(i+1, B[j])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                A.insert(i, B[j])
                j += 1

        if i >= len(A):
            # move all remaining elements from B to A
            for k in range(j, n):
                A.append(B[k])
        
        # Now A contains the merged elements from both A and B
        print A

# create an object of the class
obj = Solution()

# Inputs list A and List B
A = [1, 7, 9, 10, 11]
B = [-7, 0, 7, 11, 19, 22]

print "A : ", A
print "B : ", B
print "After Merging, A : ", obj.merge(A, B)
        