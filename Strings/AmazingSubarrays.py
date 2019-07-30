# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2019-07-30 09:13:03
# @Last Modified by:   Manju S V
# @Last Modified time: 2019-07-30 09:22:35

# You are given a string S, and you have to find all the amazing substrings of S.
# Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).


class Solution:
    # @param A : string
    # @return an integer
    def amazingSubarrays(self, S):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count = 0
        i = 0
        while i < len(S):
            if S[i] in vowels:
                count += len(S[i:])
            i += 1

        return count % 10003


# create an object of class
obj = Solution()

# take input from user
s = input("Enter the input string : ")

print("Number of Amazing Substrings in given string : ", obj.amazingSubarrays(s))
