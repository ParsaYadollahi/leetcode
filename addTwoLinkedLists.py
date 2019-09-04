# https://leetcode.com/problems/add-two-numbers/

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self):
        n = self.head
        while n is not None:
            print(n.data, end = '\t')
            n = n.next
        print('')
        
    def insert(self, data):
        new_item = Node(data)
        new_item.next = self.head
        self.head = new_item

    def reverseLinkedList(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
    

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    ret_node = linkedList()

    head1 = l1.head
    head2 = l2.head
    carry = 0

    datalist1 = head1.data
    datalist2 = head2.data
    sum = (datalist1 + datalist2 + carry)
    data = sum%10
    ret_node.insert(data)

    while(head1.next is not None):
        head1 = head1.next
        head2 = head2.next

        datalist1 = head1.data
        datalist2 = head2.data
        sum = (datalist1 + datalist2 + carry)

        data = sum%10
        carry = int(sum/10)
        ret_node.insert(data)

    while head1.next is not None:
        ret_node.insert(head1.data)
        head1 = head1.next

    while head2.next is not None:
        ret_node.insert(head2.data)
        head2 = head2.next


    return(ret_node)

if __name__ == '__main__':
    l1 = linkedList()
    l1.insert(3)
    l1.insert(4)
    l1.insert(2)

    l2 = linkedList()
    l2.insert(4)
    l2.insert(6)
    l2.insert(5)
    l2.insert(5)


    l1.reverseLinkedList()
    l2.reverseLinkedList()

    print('Reversed')
    l1.traverse_list()
    l2.traverse_list()

    print("The Answer: ")
    answer = addTwoNumbers(l1, l2)

    answer.traverse_list()
