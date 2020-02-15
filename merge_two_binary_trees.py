'''
    https://leetcode.com/problems/merge-two-binary-trees/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def add_roots(t1, t2):

            # One of the nodes have no left
            if t1 == None:
                return t2
            if t2 == None:
                return t1

            # Create the new node
            t1.val = t1.val + t2.val

            # Add the left and right
            t1.left = add_roots(t1.left, t2.left)
            t1.right = add_roots(t1.right, t2.right)

            return t1
        return add_roots(t1, t2)
