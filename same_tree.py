'''
    https://leetcode.com/problems/same-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def traverse(p, q):
            # Both p and q are end nodes
            if (not p and not q):
                return True
            # either p is missing or q
            if (not p or not q):
                return False
            if p.val != q.val:
                return False

            rights = traverse(p.right, q.right)
            lefts = traverse(p.left, q.left)

            return (rights and lefts)

        return traverse(p, q)
