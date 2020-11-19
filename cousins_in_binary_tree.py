'''
  https://leetcode.com/problems/cousins-in-binary-tree
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        x_level = 0
        y_level = 0
        x_parent = None
        y_parent = None

        def dfs(root, x, y, level):

            if not root:
                return

            nonlocal x_level
            nonlocal y_level
            nonlocal x_parent
            nonlocal y_parent

            if (root.left and root.left.val == x or root.right and root.right.val == x):
                x_level = level + 1
                x_parent = root

            elif (root.left and root.left.val == y or root.right and root.right.val == y):
                y_level = level + 1
                y_parent = root

            dfs(root.left, x, y, level + 1)
            dfs(root.right, x, y, level + 1)

        dfs(root, x, y, 0)

        if x_parent:
            if x_level == y_level and x_parent != y_parent:
                return True
        return False
