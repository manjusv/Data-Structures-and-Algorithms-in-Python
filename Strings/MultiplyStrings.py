# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-04-06 17:45:07
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:13:41

# Given two numbers represented as strings, return multiplication of the numbers as a string.


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        sum = 0
        B = B[::-1]
        for i in range(len(B)):
            s = int(A) * int(B[i])
            # Append i zeros at end
            s = str(s) + "0" * i
            sum += int(s)

        return str(sum)


# create an object of the class
obj = Solution()

print "Result after Multiplying : ", obj.multiply("513184815557478470326963292290492102373370", "56675688419586288442134264892419611145485574406534291250836")
