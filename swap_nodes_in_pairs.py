'''
https://leetcode.com/problems/swap-nodes-in-pairs/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        def pair_swap(head):

            if head and head.next: # at least have two nodes to swap
                
                rec = pair_swap(head.next.next)
                
                # swap current
                tmp = head.next
                head.next = rec
                tmp.next = head
                return tmp

            else:
                
                return head
            
        return pair_swap(head)
        