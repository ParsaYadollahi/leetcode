'''
  https://leetcode.com/problems/palindrome-linked-list/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head

        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

        reversed_half_linkedList = self.reverse_LL(slow)

        x = reversed_half_linkedList
        fast = head

        while(reversed_half_linkedList is not None and fast is not None):
            if (reversed_half_linkedList.val != fast.val):
                return False
            reversed_half_linkedList, fast = reversed_half_linkedList.next, fast.next

        return True

    def reverse_LL(self, head):

        prev = None
        current = head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return prev
