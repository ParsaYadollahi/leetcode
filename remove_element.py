class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)
        i = 0
        while(i < k):
            if (nums[i] == val):
                nums.pop(i)
                k-=1
            else:
                i+=1
        return(len(nums))
