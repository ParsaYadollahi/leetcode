'''
    https://leetcode.com/problems/maximum-subarray
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#         GREEDYYYYYY
        max_sum = max(nums)
        current_sum = nums[0]
        for n in nums[1:]:
            if (n >= current_sum + n):
                current_sum = n
            else:
                current_sum += n

            max_sum = max(current_sum, max_sum)

        return max_sum
