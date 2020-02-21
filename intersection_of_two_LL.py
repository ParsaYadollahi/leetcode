# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_A = 0
        len_B = 0
        head_a = headA
        head_b = headB
        while (headA != None):
            len_A += 1
            headA = headA.next

        while (headB != None):
            len_B += 1
            headB = headB.next

        intersect_node = abs(len_A - len_B)

        ret_node = None
        if len_A > len_B:
            for i in range(intersect_node):
                head_a = head_a.next
            ret_node = head_a

        if len_A < len_B:
            for i in range(intersect_node):
                head_b = head_b.next
            ret_node = head_b

        while head_a and head_b:
            if head_a is head_b:
                return head_a
            head_a = head_a.next
            head_b = head_b.next
        return None
