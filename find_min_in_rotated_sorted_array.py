'''
    https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/206/
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        elif len(nums) == 0:
            return nums[0]

        l = 0
        r = len(nums)-1
        mid = len(nums)//2

        while(l < r):
            if nums[l] > nums[mid] or nums[l] < nums[r]:
                r = mid
            else:
                l = mid+1
            mid = (l+r)//2

        return nums[l]
