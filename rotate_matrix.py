'''
  https://leetcode.com/problems/rotate-image/
'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n//2 + n % 2):
            for j in range(n//2):
                row, col = i, j
                temp_array = [0]*4

                for k in range(4):
                    temp_array[k] = matrix[row][col]
                    row, col = col, n-1-row

                for k in range(4):
                    matrix[row][col] = temp_array[(k-1) % 4]
                    row, col = col, n-1-row
