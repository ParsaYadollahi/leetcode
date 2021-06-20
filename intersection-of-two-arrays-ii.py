'''
    https://leetcode.com/problems/intersection-of-two-arrays-ii
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []

        for i in nums1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for i in nums2:
            if i in d and d[i] > 0:
                res.append(i)
                d[i] -= 1

        return res
