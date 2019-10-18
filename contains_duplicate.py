class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ret_dict = {}
        for i, n in enumerate(nums):
            if n not in ret_dict:
                ret_dict.setdefault(n, i)
            else:
                return True
        return False

        # could also do
        ####
        # return len(nums) - len(collections.Counter(nums)) > 0