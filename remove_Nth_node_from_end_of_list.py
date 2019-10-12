'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head
        p1 = current
        
        if p1.next == None: # single node case
            return
        
        for i in range(n):
            p1 =  p1.next

        if p1 == None: # n = length of list case
            head = head.next
            return head

        p2 = current
        while(p1.next != None):
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next

        return head