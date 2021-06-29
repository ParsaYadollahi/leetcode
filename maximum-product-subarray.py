'''
    https://leetcode.com/problems/maximum-product-subarray
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_max = 1
        curr_min = 1

        for n in nums:
            if n == 0:
                curr_max = 1
                curr_min = 1
                continue

            tmp = curr_max * n
            curr_max = max(curr_max * n, curr_min * n, n)
            curr_min = min(tmp, curr_min * n, n)

            res = max(curr_max, res)

        return res
