# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-18 01:10:20
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-18 01:51:17

# Given two binary strings, return their sum (also a binary string)

class Solution:
    # Function to return sum and carry
    def sumDigits(self, digit1, digit2, carry):
        if digit1 == '0' and digit2 == '0' and carry == 0:
            return [0, 0]
        elif digit1 == '0' and digit2 == '0' and carry == 1:
            return [1, 0]
        elif (digit1 == '0' and digit2 == '1' and carry == 0):
            return [1, 0]
        elif (digit1 == '0' and digit2 == '1' and carry == 1):
            return [0, 1]
        elif (digit1 == '1' and digit2 == '0' and carry == 0):
            return [1, 0]
        elif (digit1 == '1' and digit2 == '0' and carry == 1):
            return [0, 1]
        elif (digit1 == '1' and digit2 == '1' and carry == 0):
            return [0, 1]
        else:
            return [1, 1]
            
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        i = len(A) - 1
        j = len(B) - 1
        # result string
        res_str = ''
        # take carry as 0 in beginning
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                s1 = A[i]
            else:
                s1 = '0'
            if j >= 0:
                s2 = B[j]
            else:
                s2 = '0'
            res = self.sumDigits(s1, s2, carry)
            sum1, carry = res[0], res[1]
            res_str = res_str + str(sum1)
            i -= 1
            j -= 1
        # append the carry at end
        if carry == 1:
            res_str = res_str + str(carry)
        # return the result
        return res_str[::-1]

# create an object of the class
obj = Solution()

# Input two strings
string1 = raw_input("Enter binary string 1 : ")
string2 = raw_input("Enter binary string 2 : ")

print "Sum of two given binary strings as a binary string : ", obj.addBinary(string1, string2)