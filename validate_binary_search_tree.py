'''
  https://leetcode.com/problems/validate-binary-search-tree
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        nums = []

        def inorder_traversal(root):
            if root is None:
                return
            inorder_traversal(root.left)
            nums.append(root.val)
            inorder_traversal(root.right)

        inorder_traversal(root)
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False
        return True
