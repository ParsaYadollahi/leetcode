'''
    https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/207/
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        elif len(nums) == 0:
            return nums[0]

        l = 0
        r = len(nums)-1
        mid = (r)//2

        while(l < r):
            # mid = l + (r-l) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
            mid = (l+r)//2

        return nums[l]
