'''
  https://leetcode.com/problems/sort-the-matrix-diagonally/
  surprisingly figured this one out quickly
'''


# class Solution:
#     def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

#         if len(mat) == 1:
#             return mat

#         r, c = len(mat), 0

#         while (r >= 0):
#             self.sort_diag(mat, r, 0)
#             r -= 1

#         while (c <= len(mat[0])):
#             self.sort_diag(mat, 0, c)
#             c += 1

#         return mat

#     def sort_diag(self, mat, row, col):
#         temp_row, temp_col = row, col
#         l = []
#         while (row < len(mat) and col < len(mat[0])):
#             l.append(mat[row][col])
#             row += 1
#             col += 1

#         l.sort()
#         row, col = temp_row, temp_col
#         for e in l:
#             mat[row][col] = e
#             row += 1
#             col += 1

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        self.num_rows = len(mat)
        self.num_cols = len(mat[0])
        if len(mat) == 1:
            return mat

        r, c = 0, 1

        while (r <= self.num_rows):
            self.sort_diag(mat, r, 0)
            r += 1

        while (c <= self.num_cols):
            self.sort_diag(mat, 0, c)
            c += 1

        return mat

    def sort_diag(self, mat, row, col):
        temp_row, temp_col = row, col
        l = []
        while (row < self.num_rows and col < self.num_cols):
            l.append(mat[row][col])
            row += 1
            col += 1

        l.sort()
        row, col = temp_row, temp_col
        for e in l:
            mat[row][col] = e
            row += 1
            col += 1
