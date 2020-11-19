'''
  https://leetcode.com/problems/minimum-distance-between-bst-nodes
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        tot_min = 9999
        nodes = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)

        inorder(root)

        for i in range(len(nodes) - 1):
            tot_min = min(tot_min, nodes[i+1] - nodes[i])

        return tot_min
