# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-04 21:12:42
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:35:28


class Solution():
    # Function to find intersection of two sorted lists
    def Intersect(self, list1, list2):
        i = 0
        j = 0
        result = []
        while i < len(list1) and j < len(list2):
            if list1[i] == list2[j]:
                result.append(list1[i])
                i += 1
                j += 1
            elif list1[i] < list2[j]:
                i += 1
            else:
                j += 1
        return result


# create an object of class Solution
obj = Solution()

# input two sorted lists
A = [1, 2, 3, 3, 4, 5, 6]
B = [3, 3, 5]

print "Intersection of given sorted lists : ", obj.Intersect(A, B)
