# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-04-12 17:05:24
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-12 18:48:32

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
# P.......A........H.......N
# ..A..P....L....S....I...I....G
# ....Y.........I........R

# And then read line by line: PAHNAPLSIIGYIR which should be the output


class Solution:
    # @param S : string
    # @param rows : rows
    # @return a string
    def convert(self, S, rows):
        # create a 2D matrix
        if rows <= 1:
            return S
        n = len(S)
        res = ''
        matrix = [[''] * n for row in range(rows)]
        down = True
        i = 0
        # column represents the current column in marix we are filling
        column = 0
        while i < n:
            # fill the matrix in forward direction
            if down:
                j = 0 if i == 0 else 1
                while i < n and j < rows and column < n:
                    matrix[j][column] = S[i]
                    i += 1
                    j += 1
                else:
                    down = False
                    column += 1
            # fill the matrix in backward direction
            else:
                j = (rows - 1) - 1
                while i < n and j >= 0 and column < n:
                    matrix[j][column] = S[i]
                    i += 1
                    j -= 1
                else:
                    down = True
                    column += 1

        for l in range(len(matrix)):
            for m in range(len(matrix[l])):
                if matrix[l][m]:
                    res += matrix[l][m]
        return res


# create an object of the class
obj = Solution()

input = "IMDOINGGOOD"


print "Zig Zag output : ", obj.convert(input, 4)
