class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bad problem
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        slow = 1
        for fast in range(len(nums)):
            if nums[fast] != nums[slow-1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow
