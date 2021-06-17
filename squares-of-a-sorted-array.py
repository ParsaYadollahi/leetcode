'''
    https://leetcode.com/problems/squares-of-a-sorted-array
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def squared(num):
            return num ** 2

        if len(nums) == 1:
            return [squared(nums[0])]

        new_nums = [0] * len(nums)
        l, r = 0, len(nums) - 1

        while (l <= r):
            left, right = squared(nums[l]), squared(nums[r])
            if (left > right):
                new_nums[r-l] = left
                l += 1
            else:
                new_nums[r-l] = right
                r -= 1


        return new_nums
