'''
  https://leetcode.com/problems/binary-tree-level-order-traversal-ii\
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        nodes = []
        level = 0

        def dfs(root, level):
            if (root is None):
                return

            if (len(nodes)-1 < level):
                nodes.append([root.val])

            else:
                nodes[level].append(root.val)

            dfs(root.left, level+1)
            dfs(root.right, level+1)

        dfs(root, level)
        return nodes[::-1]
