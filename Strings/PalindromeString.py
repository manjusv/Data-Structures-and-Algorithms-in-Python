# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-06 18:05:59
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-06 18:12:34

# Program to determine if a given string is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution:
    # @param strr : string
    # @return True or False
    def isPalindrome(self, strr):
    	# Convert all characters to lower case
        strr = strr.lower()
        n = len(strr)
        i = 0
        j = n - 1
        while(i < j):
            if(strr[i].isalnum() and strr[j].isalnum()):
                if(strr[i] != strr[j]):
                    return False
                i = i + 1
                j = j - 1
            elif(strr[i].isalnum() == False and strr[j].isalnum() == False):
                i = i + 1
                j = j - 1
            elif(strr[i].isalnum()):
                j = j - 1
            else:
                i = i + 1
        return True

# create an obj of the class
obj = Solution()

input_string = "He is, a good !boy yob doog a si eh"

if obj.isPalindrome(input_string):
	print "It is a palindrome string"
else:
	print "Not a palindrome"