'''
    https://leetcode.com/explore/interview/card/microsoft/32/linked-list/205/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        carry = 0
        sum = l1.val + l2.val + carry
        carry = sum//10
        sum = sum % 10

        begining = prev = ListNode(sum)
        l1, l2 = l1.next, l2.next
        head = prev
        new_node = ListNode(0)

        while(l1 != None and l2 != None):
            sum = l1.val + l2.val + carry
            carry = sum//10
            sum = sum % 10

            new_node = ListNode(sum)
            prev.next = new_node

            prev = new_node
            l1, l2 = l1.next, l2.next

        if l1 == None and l2 != None:
            while(l2 != None):
                sum = (l2.val+carry)
                prev.next = ListNode(sum % 10)
                carry = sum//10
                l2, prev = l2.next, prev.next
                print(carry)
        if l2 == None and l1 != None:
            while(l1 != None):
                sum = (l1.val+carry)
                prev.next = ListNode(sum % 10)
                carry = sum//10
                l1, prev = l1.next, prev.next

        prev.next = ListNode(carry) if carry else None
        return self.reverse(begining)

    def reverse(self, l: ListNode) -> ListNode:
        prev = None
        while(l != None):
            next = l.next
            l.next = prev
            prev = l
            l = next
        l = prev
        return l
