'''
  https://leetcode.com/problems/non-decreasing-array/
'''

class Solution: # my solution
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                if (i == 0):
                    nums.pop(i)
                elif nums[i-1] <= nums[i+1]:
                    nums.pop(i)
                else:
                    nums.pop(i+1)
                break

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False

        return True



class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        check =  False

        if len(nums) <= 1:
            return True

        for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    if check == False:
                        if (i == 0):
                            nums[i] = nums[i+1]
                        elif nums[i-1] <= nums[i+1]:
                            nums[i] = nums[i-1]
                        else:
                            nums[i+1] = nums[i]
                        check = True
                    else:
                        return False

        return True
