'''
  https://leetcode.com/problems/linked-list-random-node
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.num_nodes = 0
        self.head = head

        while (head is not None):
            self.num_nodes += 1
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        r = random.randint(0, self.num_nodes-1)
        head = self.head
        for i in range(r):
            head = head.next

        return head.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
