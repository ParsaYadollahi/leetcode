'''
    https://leetcode.com/explore/interview/card/microsoft/31/trees-and-graphs/164/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret_arr = []
        levels = 0
        if not root:
            return ret_arr

        def helper(node, levels, ret_arr):
            if len(ret_arr) == levels:
                ret_arr.append([])

            ret_arr[levels].append(node.val)

            if node.left:
                helper(node.left, levels + 1, ret_arr)
            if node.right:
                helper(node.right, levels + 1, ret_arr)

            return ret_arr
        return helper(root, levels, ret_arr)
