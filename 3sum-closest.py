'''
    https://leetcode.com/problems/3sum-closest
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_target = 10**3
        ret_target = 0

        for i in range(len(nums)):
            p1, p2 = i + 1, len(nums) - 1
            while(p1 < p2):
                sum = nums[i] + nums[p1] + nums[p2]
                if (abs(target - sum) < abs(min_target)):
                    min_target = target - sum

                if sum > target:
                    p2 -= 1
                elif sum < target:
                    p1 += 1
                else:
                    return target - min_target
        return target - min_target
