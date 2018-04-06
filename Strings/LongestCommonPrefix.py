# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-04-06 14:45:02
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 15:18:18

# longest common prefix string amongst an array of strings.


class Solution:
    # @param strings : list of strings
    # @return a string
    def longestCommonPrefix(self, strings):
        if "" in strings:
            return ""
        # find the min length string from the list
        mString = min(strings, key=len)

        while True:
            if mString == "":
                break
            tstrings = [s[:len(mString)] for s in strings]
            # if min string matches with all, return mString
            if all(mString == item for item in tstrings):
                return mString
            else:
                # remove last char to check for next possible prefix
                mString = mString[:-1]

        return mString


# create an object of the class
obj = Solution()

# Input a list of strings
input_string = ["abcfd", "abdcde", "abcf"]
print "Longest Common Prefix  : ", obj.longestCommonPrefix(input_string)
