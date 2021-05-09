'''
    https://leetcode.com/problems/jump-game-ii
'''
class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return 0

        ret_val = 1
        i = 0
        while(i + nums[i] < len(nums)-1):
            i = self.best_jump(nums, nums[i], i + 1)
            ret_val += 1
        return ret_val

    def best_jump(self, nums, dist, index):
        max_dist = 0
        ret_index = 0

        for i in range(dist):
            if i + index > len(nums):
                break
            if (max_dist < nums[i+index] + i):
                max_dist = nums[i+index] + i
                ret_index = i + index

        return ret_index
