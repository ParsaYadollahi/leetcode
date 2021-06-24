'''
    https://leetcode.com/problems/search-in-rotated-sorted-array
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return []
        left = 0
        right = len(nums) - 1

        while(left < right):

            midpoint = (right + left) // 2

            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint

        smallest = left
        left = 0
        right = len(nums) - 1

        if (nums[smallest] <= target and nums[right] >= target):
            left = smallest
        else:
            right = smallest

        while(left <= right):
            midpoint = (left + right) // 2
            if nums[midpoint] == target:
                return midpoint

            elif (nums[midpoint] < target):
                left = midpoint + 1
            else:
                right = midpoint - 1

        return -1
