'''
  https://leetcode.com/problems/max-consecutive-ones
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        temp = 0
        for i in nums:
            if i == 1:
                temp += 1

            if temp > max_ones:
                    max_ones = temp
            if i != 1:
                temp = 0

        return max_ones
