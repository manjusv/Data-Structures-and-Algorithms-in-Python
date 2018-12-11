# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-04-23 19:45:26
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-23 20:13:42


class Solution:
    def isPalindrome(self, s):
        reverse_s = s[::-1]
        if s == reverse_s:
            return True
        return False

    # @param s : string
    # @return a strings
    def _longestPalindrome(self, s, i, j):
        if self.isPalindrome(s[i:j]):
            return s[i:j]
        elif self.isPalindrome(s[i:j - 1]):
            return s[i:j - 1]
        elif self.isPalindrome(s[i + 1:j]):
            return s[i + 1:j]
        return self._longestPalindrome(s, i + 1, j - 1)

    def longestPalindrome(self, s):
        n = len(s)
        table = [[0 for x in range(n)] for y
                 in range(n)]

        # All substrings of length 1 are
        # palindromes
        maxLength = 1
        i = 0
        while (i < n):
            table[i][i] = True
            i = i + 1

        # check for sub-string of length 2.
        start = 0
        i = 0
        while i < n - 1:
            if (s[i] == s[i + 1]):
                table[i][i + 1] = True
                start = i
                maxLength = 2
            i = i + 1

        # Check for lengths greater than 2.
        # k is length of substring
        k = 3
        while k <= n:
            # Fix the starting index
            i = 0
            while i < (n - k + 1):

                # Get the ending index of
                # substring from starting
                # index i and length k
                j = i + k - 1

                # checking for sub-string from
                # ith index to jth index iff
                # st[i+1] to st[(j-1)] is a
                # palindrome
                if (table[i + 1][j - 1] and
                        s[i] == s[j]):
                    table[i][j] = True

                    if (k > maxLength):
                        start = i
                        maxLength = k
                i = i + 1
            k = k + 1

        return s[start:start + maxLength]


# create an object of class
obj = Solution()

# take input from user
s = raw_input("Enter the input string : ")

print "length of last word in given string : ", obj.longestPalindrome(s)
