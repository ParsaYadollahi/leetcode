'''
    https://leetcode.com/explore/interview/card/microsoft/32/linked-list/184/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node1 = head
        node2 = head
        while(True):
            if ((node1 == None or node2 == None) or (node1.next == None or node2.next == None)):
                return False
            else:
                node1 = node1.next
                node2 = node2.next.next
            if (node1 == node2):
                return True
