# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-21 19:20:08
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:19:08

# Compute and return the square root of x. If x is not a perfect square, return floor(sqrt(x))


class Solution:
    # @param x : integer
    # @return an integer
    def sqrt(self, x):
        if x == 0 or x == 1:
            return x
        low = 0
        high = x
        result = 0
        while low <= high:
            # Find mid
            mid = low + (high - low) / 2
            # if mid is the sqrt, return mid
            if mid * mid == x:
                return mid
            # if mid * mid is less, then traverse right side
            elif mid * mid < x:
                result = mid
                low = mid + 1
            # if mid * mid is greater than x, then traverse left side
            elif mid * mid > x:
                high = mid - 1
        return result


# create an object of the class
obj = Solution()

# Take input from user
x = input("Enter a number to find Square root : ")

print "Square root of given number : ", obj.sqrt(x)
