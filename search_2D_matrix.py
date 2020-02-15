'''
    https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/154/
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])

        left = 0  # aim for first element in entire 2d array
        right = m * n - 1  # aim for last element in entire 2d array

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            else:
                if matrix[mid // n][mid % n] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
