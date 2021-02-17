'''
  https://leetcode.com/problems/increasing-order-search-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root, l):

            if root is None:
                return

            inorder(root.left, l)
            if root is not None:
                l.append(root.val)
            inorder(root.right, l)

            return l

        head = start = TreeNode()
        l = inorder(root, [])

        for i in l:
            head.right = TreeNode(val=i)
            head = head.right

        return start.right
