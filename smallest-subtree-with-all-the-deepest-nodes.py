'''
  https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/submissions/
  Took me like an hour.. my trees leetcode is terrible
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # Tag each node with it's depth.
        depth = {None: -1}

        def dfs(node, parent):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root, None)

        max_depth = max(depth.values())

        def output(node):
            if not node or depth[node] == max_depth:
                return node

            left = output(node.left)
            right = output(node.right)

            if left and right:  # found the common parent
                return node
            else:
                return left or right

        return output(root)
