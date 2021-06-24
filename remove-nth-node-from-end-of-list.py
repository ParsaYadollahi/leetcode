'''
    https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return None

        first = head
        for i in range(n):
            first = first.next

        if first is None:
            return head.next
        second = head
        while(first is not None and first.next is not None):
            first = first.next
            second = second.next

        second.next = second.next.next
        return head
