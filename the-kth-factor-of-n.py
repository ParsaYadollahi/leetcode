'''
  https://leetcode.com/problems/the-kth-factor-of-n
'''


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        prev = None
        for i in range(1, n+1):
            if n % i == 0:
                prev = i
                k -= 1

            if k == 0:
                return prev

        return -1
