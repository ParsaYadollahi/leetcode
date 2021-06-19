'''
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = []
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1

        for i, v in enumerate(nums):
            if v > 0:
                missing.append(i+1)

        return missing
