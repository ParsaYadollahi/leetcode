'''
    https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/203/
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for c in range(len(matrix)):
            for r in range(len(matrix[0])):
                if matrix[c][r] == 0:
                    self.set_col_neg(matrix, r)
                    self.set_row_neg(matrix, c)

        for c in range(len(matrix)):
            for r in range(len(matrix[0])):
                if matrix[c][r] == '.':
                    matrix[c][r] = 0

    def set_col_neg(self, matrix, r):
        for row in range(len(matrix)):  # number of columns
            if matrix[row][r] != 0:
                matrix[row][r] = '.'

    def set_row_neg(self, matrix, c):
        for col in range(len(matrix[0])):  # number of columns
            if matrix[c][col] != 0:
                matrix[c][col] = '.'
