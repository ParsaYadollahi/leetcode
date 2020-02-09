"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
'''
    https://leetcode.com/problems/inorder-successor-in-bst-ii/
'''


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if (node.right):
            return self.goLeft(node.right)
        else:
            return self.goUp(node, node.val)

    def goUp(self, node, value):
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent

    def goLeft(self, node):
        while node.left:
            node = node.left
        return node
