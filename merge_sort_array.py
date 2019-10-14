'''
https://leetcode.com/problems/merge-sorted-array/
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        m-=1
        n-=1
        for i in range(n+m+1,-1,-1):
            if nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1

            elif nums1[m] < nums2[n]:
                nums1[i] = nums2[n]
                n -= 1
            elif nums1[m] == nums2[n]:
                nums1[i] = nums2[n]
                n-=1

            if n < 0 or m < 0:
                break

        if m < 0:
            for i in range(n+1):
                nums1[i] = nums2[i]