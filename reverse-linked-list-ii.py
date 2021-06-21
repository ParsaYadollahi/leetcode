'''
    https://leetcode.com/problems/reverse-linked-list-ii
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if head.next is None or m == n:
            return head

        ret_head = head

        first = head
        last = head

        for i in range(1, m - 1):
            first = first.next

        for i in range(1, n + 1):
            last = last.next

        if m == 1:
            first = self.reverse(first, n-m)
        else:
            first.next = self.reverse(first.next, n-m)

        head = first
        while(head.next is not None):
            head = head.next
        head.next = last

        if m == 1: return first
        return ret_head


    def reverse(self, head, m):

        prev = None
        for i in range(m + 1):
            head.next, prev, head = prev, head, head.next

        return prev
