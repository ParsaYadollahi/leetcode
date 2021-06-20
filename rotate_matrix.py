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


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.flip_matrix(matrix)
        self.tilt_matrix(matrix)

    def flip_matrix(self, matrix):
        length = len(matrix) - 1

        for i in range((length + 1) // 2):
            for j in range((length + 1)):
                matrix[i][j], matrix[length - i][j] = matrix[length - i][j], matrix[i][j]


    def tilt_matrix(self, matrix):
        length = len(matrix)
        box, i = 0, 0
        while(i <= length):
            j = box
            while(j < length):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                j += 1
            i += 1
            box += 1
