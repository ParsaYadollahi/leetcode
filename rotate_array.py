'''
  https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/
'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_arr = len(nums) - 1
        for j in range(k):
            for i in range(1, len_arr+1):
                nums[len_arr-i+1], nums[len_arr -
                                        i] = nums[len_arr-i], nums[len_arr-i+1]

        return nums
