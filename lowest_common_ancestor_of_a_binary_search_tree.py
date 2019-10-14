'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # note: read beforehand what the prog wants you te return...
        def traverse(root, p, q):

            if root == None:
                return root

            if p.val > root.val and q.val > root.val:
                return traverse(root.right, p , q)

            elif p.val < root.val and q.val < root.val:
                return traverse(root.left, p , q)

            else:
                return root

        return traverse(root, p , q)