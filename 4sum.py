'''
    https://leetcode.com/problems/4sum
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []


        for i in range(len(nums)):
            new_target = target - nums[i]

            threesum = self.threeSum(nums[i+1:], new_target)
            if threesum == [-1,-1,-1]:
                continue
            else:
                for r in threesum:
                    if [nums[i], r[0], r[1], r[2]] not in res:
                        res.append([nums[i], r[0], r[1], r[2]])
        return res

    def threeSum(self, nums, target):
        res = []

        for i in range(len(nums)):
            new_target = target - nums[i]

            twosum = self.twoSum(nums[i+1:], new_target)
            if (twosum == [-1,-1]):
                continue
            else:
                for r in twosum:
                    if [[nums[i], r[0], r[1]]] not in res:
                        res.append([nums[i], r[0], r[1]])

        if len(res) == 0:
            return [-1,-1,-1]
        else:
            return res



    def twoSum(self, nums, target):
        p1 = 0
        p2 = len(nums) - 1
        res = []
        while(p1 < p2):
            sum = nums[p1] + nums[p2]
            if sum == target and [nums[p1], nums[p2]] not in res:
                res.append([nums[p1], nums[p2]])
                p1 += 1
            elif (sum < target):
                p1 += 1
            else:
                p2 -= 1


        if len(res) == 0:
            return [-1, -1]
        else:
            return res
