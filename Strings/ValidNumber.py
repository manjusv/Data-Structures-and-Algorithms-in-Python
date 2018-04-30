# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-04-30 14:20:38
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-30 14:33:58

# https://www.interviewbit.com/problems/valid-number/


class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        # remove leading and trailing spaces
        A = A.strip()
        if len(A) == 0:
            return 0
        if ' ' in A:
            return 0
        if A.count('e') >= 2:
            return 0
        if 'e' in A:
            l = A.split('e')
            if len(l[0]) == 0 or len(l[1]) == 0:
                return 0
            # if '.' in exponent return 0
            if '.' in l[1]:
                return 0
            if l[0][-1] == '.':
                return 0
            if l[1][0] == '+' or l[1][0] == '-':
                l[1] = l[1][1:]
            if l[1].isdigit() is False:
                return 0
            if l[0][0] == '+' or l[0][0] == '-':
                l[0] = l[0][1:]
            # remove '.' if any in l[0]
            if '.' in l[0]:
                l[0] = ''.join(l[0].split('.'))
                if l[0].isdigit() is False:
                    return 0
            A = ''.join(l)
        if A.count('.') >= 2:
            return 0
        if A[0] == '+' or A[0] == '-':
            A = A[1:]
        if '.' in A:
            if A[-1] == '.':
                return 0
            A = ''.join(A.split('.'))
            if A.isdigit() is False:
                return 0
        # remove 'e' if any
        A = A.replace('e', '')
        if A.isdigit() is False:
            return 0
        return 1


# create an object of the class
obj = Solution()

input = raw_input("Enter the string : ")

print "The return value : ", obj.isNumber(input)
