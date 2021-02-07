'''
  https://leetcode.com/problems/kth-largest-element-in-an-array/
  I needa review my heaps
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 or not nums:
            return -1

        heap = []

        for num in nums:
            heappush(heap, -num)

        ret_val = None
        while (k != 0):
            ret_val = heappop(heap)
            k -= 1

        return -ret_val
