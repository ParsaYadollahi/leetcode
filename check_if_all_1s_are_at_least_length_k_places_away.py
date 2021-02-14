'''
  https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
'''


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        counter = k
        for i in nums:
            if i == 1:
                if counter < k:
                    return False
                counter = 0
            else:
                counter += 1

        return True
