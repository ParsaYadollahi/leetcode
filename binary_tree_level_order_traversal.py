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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        nodes = []

        def dfs(root, level):
            if (root == None):
                return

            if (len(nodes)-1 < level):
                nodes.append([root.val])
            else:
                nodes[level].append(root.val)

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return nodes
