'''
  https://leetcode.com/problems/spiral-matrix-ii
  Honestly.... this took waaay too long. These spiral matrices qsts built diff
'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0 for i in range(n)] for j in range(n)]
        count = 1

        for layer in range((n+1)//2):

            # Left to right
            for i in range(layer, n-layer):
                output[layer][i] = count
                count += 1

            # Top to bottom
            for i in range(layer + 1, n-layer):
                output[i][n-layer-1] = count
                count += 1

            # Right to left
            for i in range(n - layer - 2, layer - 1, -1):
                output[n-layer-1][i] = count
                count += 1

            # bottom to top
            for i in range(n - layer - 2, layer, -1):
                output[i][layer] = count
                count += 1

        return output
