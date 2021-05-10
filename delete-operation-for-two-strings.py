'''
    https://leetcode.com/problems/delete-operation-for-two-strings/
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if (i == 0 or j == 0):
                    dp[i][j] = i + j
                elif word1[i-1] != word2[j-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = dp[i-1][j-1]

        return(dp[len(word1)][len(word2)])
