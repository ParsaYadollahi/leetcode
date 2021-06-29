'''
    https://leetcode.com/problems/product-of-array-except-self
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_nums = [0] * len(nums)
        right_nums = [0] * len(nums)


        length = len(nums) - 1
        right_nums[length] = 1
        left_nums[0] = 1

        for i in range(1, len(nums)):
            left_nums[i] = left_nums[i-1] * nums[i - 1]

        for i in range(length - 1, -1, -1):
            right_nums[i] = right_nums[i + 1] * nums[i + 1]

        for i in range(length + 1):
            right_nums[i] *= left_nums[i]


        return right_nums
