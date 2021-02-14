'''
    https://leetcode.com/problems/merge-k-sorted-lists/
    Honestly tried to do O(1) space but gave up yo vaaague this is much easier
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = start = ListNode()

        arr = []
        for i in range(len(lists)):
            e = lists[i]
            while (e):
                arr.append(e.val)
                e = e.next

        for i in sorted(arr):
            head.next = ListNode(val=i)
            head = head.next

        return start.next
