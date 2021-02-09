'''
  https://leetcode.com/problems/count-sorted-vowel-strings/
  honestly I wouldn't of thought of this solution... so rip again
'''


class Solution:
    def countVowelStrings(self, n: int) -> int:

        #         a = 5
        #         e = 4
        #         i = 3
        #         o = 2
        #         u = 1

        #         for k in range(0, n-1):
        #             u=u
        #             o=o+u
        #             i=i+o
        #             e=e+i
        #             a=a+e

        #         return a
        dp = [[0 for i in range(6)] for j in range(n+1)]

        for i in range(1, 6):
            dp[1][i] = i

        for i in range(2, n+1):
            dp[i][1] = 1
            for j in range(2, 6):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                print(dp)

        return dp[n][5]
