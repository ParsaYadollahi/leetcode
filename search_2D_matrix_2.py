'''
    https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/195/
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        col = 0
        # Start at bottom left of matrix
        while (row >= 0 and col <= len(matrix[0])-1):

            # Found target
            if matrix[row][col] == target:
                return True

            if matrix[row][col] > target:
                row -= 1
            if matrix[row][col] < target:
                col += 1
        return False
