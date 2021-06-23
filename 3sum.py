'''
    https://leetcode.com/problems/3sum
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            target = -nums[i]
            twoSumRet = self.twoSum(nums[i+1:], target, i+1)

            if twoSumRet == [-1,-1]:
                continue
            else:
                for e in twoSumRet:
                    input = [nums[i], e[0], e[1]]
                    if input not in res:
                        res.append(input)

        return res

    def twoSum(self, nums, target, i):
        p1 = 0
        p2 = len(nums) - 1
        res = []


        while (p1 < p2):
            if nums[p1] + nums[p2] < target:
                p1 += 1
            elif nums[p1] + nums[p2] > target:
                p2 -= 1
            else:
                res.append([nums[p1], nums[p2]])
                p1 += 1

        if len(res) != 0:
            return res
        else:
            return [-1,-1]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(nums)-1):
            target = -nums[i]
            twoSumRet = self.twoSum(nums[i+1:], target, i+1)

            if twoSumRet == []:
                continue
            else:
                for e in twoSumRet:
                    input = sorted([nums[i], e[0], e[1]])
                    if input not in res:
                        res.append(input)

        return res

    def twoSum(self, nums, target, i):
        d = {}
        res = []

        for i in nums:
            if target - i not in d:
                d[i] = i
            else:
                res.append([i, d[target-i]])

        return res
