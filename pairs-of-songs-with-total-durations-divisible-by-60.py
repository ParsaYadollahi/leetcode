'''
  https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
  Nooooooot even gonna kap, no way I woulda found this ans out
'''


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        remainder = [0] * 60

        output = 0
        for i in time:
            if i % 60 == 0:
                output += remainder[0]
            else:
                output += remainder[60 - i % 60]

            remainder[i % 60] += 1
        return output
