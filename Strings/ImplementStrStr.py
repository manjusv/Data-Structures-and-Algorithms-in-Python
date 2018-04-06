# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-28 09:40:08
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:29:36

# locate a substring ( needle ) in a string ( haystack ).Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        m = len(A)
        n = len(B)
        if n == 0 or (m == 0 and n == 0) or (m < n):
            return -1
        j = 0
        for i in range(0, m - n + 1):
            # if first character of B matches with any character of A
            if B[j] == A[i]:
                if A[i: i + n] == B:
                    # return the start index
                    return i

        return -1


# create an object of class
obj = Solution()

# Take input from user
A = raw_input("Enter the Main String : ")
B = raw_input("Enter the SubString : ")

pos = obj.strStr(A, B)
if pos != -1:
    print "SubString found at position : ", pos
else:
    print "Substring Not Found!"
