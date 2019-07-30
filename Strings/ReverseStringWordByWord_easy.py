# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2019-07-30 10:05:05
# @Last Modified by:   Manju S V
# @Last Modified time: 2019-07-30 10:05:50

# Program to reverse a given string word by word
# Input - "This is very cool"
# Output - "cool very is This"


class Solution:
    # @param S : string
    # @return string
    def reverseWords(self, S):
        S = S[::-1]
        S = [x for x in S.split()]
        for i, item in enumerate(S):
            S[i] = item[::-1]

        return ' '.join(S)


# create an object of class
obj = Solution()

# take input from user
s = input("Enter the input string : ")

print("String after reversing the words in given the string : ", obj.reverseWords(s))
