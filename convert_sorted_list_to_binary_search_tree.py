'''
  https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        if head is None:
            return
        if head.next is None:
            return TreeNode(head.val)

        slow, fast = head, head
        while (fast and fast.next):
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        prev_slow.next = None
        treeNode = TreeNode()
        treeNode.val = slow.val

        treeNode.left = self.sortedListToBST(head)
        treeNode.right = self.sortedListToBST(slow.next)

        return treeNode
