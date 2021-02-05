'''
  https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
  Feelz bad I didn't know we could use Binary search on this.... RIP maybe another day
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        ret_head = prev = ListNode(0, head)
        head
        while (head and head.next):
            if head.val == head.next.val:
                head = prev
                temp = head.next
                temp_val = head.next.val
                while(temp and temp.val == temp_val):
                    temp = temp.next
                head = temp
                prev.next = head
            else:
                head = head.next
                prev = prev.next
        return ret_head.next
