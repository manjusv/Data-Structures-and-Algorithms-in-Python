# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-04-12 11:38:59
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-12 16:26:29

# Pretty print a json object using proper indentation.

# Every inner brace should increase one indentation to the following lines.
# Every close brace should decrease one indentation to the same line and the following lines.
# The indents can be increased with an additional ‘\t’
# Input : {A:"B",C:{D:"E",F:{G:"H",I:"J"}}}
# Output :
# {
#     A:"B",
#     C:
#     {
#         D:"E",
#         F:
#         {
#             G:"H",
#             I:"J"
#         }
#     }
# }


class Solution:
    # @param S : string
    # @return a list of strings
    def prettyJSON(self, S):
        res = []
        # remove all the spaces from the input string
        S = S.replace(" ", "")
        n = len(S)
        if n == 0:
            return res
        i = 0
        tabs = 0
        temp = ''
        while i < n:
            if S[i] in ['{', '[']:
                res.append('\t' * tabs + S[i])
                tabs += 1
                i += 1
            elif S[i] in ['}', ']']:
                # res.append('\t' * tabs + temp)
                if i + 1 < n and S[i + 1] == ',':
                    res.append('\t' * tabs + S[i] + S[i + 1])
                    i += 2
                    # tabs -= 1
                else:
                    res.append('\t' * tabs + S[i])
                    i += 1
                    tabs -= 1
            elif S[i] == ',':
                res.append('\t' * tabs + temp + S[i])
                temp = ''
                i += 1
            elif S[i] == ':':
                if i + 1 < n and (S[i + 1] == '[' or S[i + 1] == '{'):
                    res.append('\t' * tabs + temp + S[i])
                    temp = ''
                else:
                    temp += S[i]
                i += 1
            else:
                temp += S[i]
                if S[i + 1] == '}' or S[i + 1] == ']':
                    res.append('\t' * tabs + temp)
                    temp = ''
                    tabs -= 1
                i += 1
        return res


# create an object of the class
obj = Solution()

input = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'

res = obj.prettyJSON(input)

for item in res:
    print item
