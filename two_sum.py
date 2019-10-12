class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for index, value in enumerate(nums):
            remainder = target - value
            
            if remainder in hash_table:
                return([index, hash_table[remainder]])
            
            hash_table[value] = index