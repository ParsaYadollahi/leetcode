'''
https://leetcode.com/problems/permutations/
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # ngl, not a big fan of recursion
        def permutations(num):
            if len(num) <= 1:
                return [num]
            ans = []
            for i in num:
                remaining_letters = [x for x in num if x != i] # append each other char

                for e in permutations(remaining_letters):
                    ans.append(e+[i])

            return ans

        ret_list = permutations(nums)
        return ret_list
