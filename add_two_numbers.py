# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = l3 = ListNode(None)
        while l1 and l2:
            sum = carry+l1.val+l2.val
            if sum >= 10:
                carry = 1
            else:
                carry = 0

            l3.next = ListNode(sum % 10)
            l1, l2, l3 = l1.next, l2.next, l3.next

        while l1:
            sum = carry+l1.val
            carry = 1 if sum >= 10 else 0
            l3.next = ListNode(sum % 10)
            l1, l3 = l1.next, l3.next

        while l2:
            sum = carry+l2.val
            carry = 1 if sum >= 10 else 0
            l3.next = ListNode(sum % 10)
            l2, l3 = l2.next, l3.next

        l3.next = ListNode(carry) if carry else None

        return head.next
