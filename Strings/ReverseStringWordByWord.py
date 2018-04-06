# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-06 18:16:13
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:31:07

# Program to reverse a given string word by word
# Input - "This is very cool"
# Output - "cool very is This"


class Solution:
    # Function to reverse a substring from index k to index l in a given string
    def ReverseString(self, A, k, l):
        str1 = ""
        while k <= l:
            str1 += A[l]
            # i = i + 1
            l = l - 1
        return str1

    # @param A : string
    # @return string
    def reverseWords(self, A):
        res = ""
        i = 0
        if len(A) == 1:
            return A
        # First reverse every word in the given string
        while i < len(A):
            if A[i] != ' ':
                j = i
                while j < len(A) and A[j] != ' ':
                    j = j + 1
                j = j - 1
                res = res + self.ReverseString(A, i, j)
                res = res + ' '
                i = j + 1
            else:
                i = i + 1

        # remove the leading or trailing spaces if any
        res = res.strip()

        # Now return the reversed string
        return res[::-1]


# create an object of a class
obj = Solution()

input_string = "This is cool"

print "The string after reversing word by word : ", obj.reverseWords(input_string)
