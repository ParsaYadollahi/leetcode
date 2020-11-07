'''
  https://leetcode.com/problems/partition-list/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1 = beginning_list_1 = ListNode(0)
        head2 = beginning_list_2 = ListNode(0)

        while(head):

            if head.val < x:
                head1.next = head
                head1 = head

            else:
                head2.next = head
                head2 = head

            head = head.next

        head2.next = None
        head1.next = beginning_list_2.next

        return beginning_list_1.next
