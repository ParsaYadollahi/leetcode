'''
    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstIndex(nums, target)
        last = self.lastIndex(nums, target)

        return [first, last]



    def firstIndex(self, nums, target):
        index = -1
        l = 0
        r = len(nums) - 1

        while(l <= r):
            m = (l+r) // 2
            if (nums[m] == target): index = m
            if (nums[m] >= target):
                r = m - 1
            else:
                l = m + 1

        return index


    def lastIndex(self, nums, target):
        index = -1
        l = 0
        r = len(nums) - 1

        while(l <= r):
            m = (l+r) // 2

            if nums[m] == target: index = m
            if (nums[m] <= target):
                l = m + 1
            else:
                r = m - 1

        return index
