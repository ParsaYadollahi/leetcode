'''
  https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not len(nums):
            return

        mid = len(nums)//2

        left, right = nums[:mid], nums[mid+1:]

        tree_node = TreeNode(nums[mid])

        tree_node.left = self.sortedArrayToBST(left)
        tree_node.right = self.sortedArrayToBST(right)

        return tree_node
