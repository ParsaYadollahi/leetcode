'''
  Remove duplicates from an unsorted linked list - CTCI #2.1
'''


class LinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:
    def remove_duplicates_from_LL(self, head):
        first_node = head
        dic = {}

        prev = head
        dic.setdefault(head.val, 1)
        head = head.next

        while (head != None):
            # print(head.val)

            if (head.val not in dic):
                dic.setdefault(head.val, 1)
                prev = head
                head = head.next

            else:
                prev.next = head.next
                head = head.next

    def print_ll(self, head):
        while (head != None):
            print(head.val)
            head = head.next


ll = LinkedList()
ll.head = Node(1)
n2 = Node(3)
n3 = Node(2)

n4 = Node(4)
n5 = Node(3)
n6 = Node(4)
n7 = Node(5)


ll.head.next = n2
n2.next = n3

n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7


s = Solution()
s.remove_duplicates_from_LL(ll.head)
s.print_ll(ll.head)
