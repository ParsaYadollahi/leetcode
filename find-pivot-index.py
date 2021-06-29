'''
    https://leetcode.com/problems/find-pivot-index
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = 0

        for n in nums:
            total_sum += n

        for i in range(len(nums)):
            if (total_sum - left_sum - nums[i] == left_sum):
                return i

            left_sum += nums[i]

        return -1
