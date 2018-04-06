# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-04-06 16:33:14
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 17:30:44

# The count-and-say sequence is the sequence of integers beginning as follows
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as one 1 or 11, 11 is read off as two 1s or 21, 21 is read off as one 2, then one 1 or 1211.
# Given an integer n, generate the nth sequence.

class Solution:
    # Function to generate next sequence
    def Next(self, s):
        length = len(s)
        res = ""
        i = 0
        while i < length:
            count = 1
            while i + 1 < length and s[i] == s[i + 1]:
                count += 1
                i += 1
            res = res + str(count) + s[i]
            i += 1

        return res

    # @param n : integer
    # @return a string
    def countAndSay(self, n):
        s = "1"
        for i in range(1, n):
            s = self.Next(s)

        return s


# create an object of the class
obj = Solution()

# Input a list of strings
n = 5
print "nth sequence  : ", obj.countAndSay(n)
