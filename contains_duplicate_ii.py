class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        j = 0
        d = {}
        while (j < len(nums)):
            if (nums[j] not in d):
                d.setdefault(nums[j], j)
                j += 1
            else:
                if j-d[nums[j]] <= k:
                    return True
                else:
                    d.update({nums[j]: j})
                    j+=1

        return False
