'''
  https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
  Sometimes its better to take the L and do O(2n) instead of O(n) and lose hairsss
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 1
        cur = nums[0]

        for i in range(1, len(nums)):

            if cur == nums[i]:
                if length < 2:
                    length += 1
                else:
                    nums[i] = None
            else:
                cur = nums[i]
                length = 1

        i, j = 0, 0
        while (j < len(nums)):
            if nums[i] is None:
                if nums[j] is None:
                    j += 1
                    continue
                else:
                    nums[i] = nums[j]
                    nums[j] = None
            i += 1
            j += 1

        return i
