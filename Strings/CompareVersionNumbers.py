# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-04-29 16:40:39
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-29 17:13:29

# Compare two version numbers version1 and version2.

# If version1 > version2 return 1,
# If version1 < version2 return -1,
# otherwise return 0.


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        # split the strings using .
        s1 = A.split('.')
        s2 = B.split('.')
        l1, l2 = len(s1), len(s2)
        length = l1 if l1 < l2 else l2

        i = 0
        while i < length:
            if int(s1[i]) > int(s2[i]):
                return 1
            elif int(s1[i]) < int(s2[i]):
                return -1
            else:
                i += 1

        if l1 == l2:
            return 0
        elif l1 > l2:
            temp = ''.join(s1[i:])
            if int(temp) == 0:
                return 0
            return 1
        else:
            temp = ''.join(s2[i:])
            if int(temp) == 0:
                return 0
            return -1


# create an object of the class
obj = Solution()

# Take input from user
A = raw_input("Enter string A(version1) : ")
B = raw_input("Enter string B(version2) : ")

print "The return value : ", obj.compareVersion(A, B)
