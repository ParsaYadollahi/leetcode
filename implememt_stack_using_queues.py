'''
    https://leetcode.com/problems/implement-stack-using-queues/
'''


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # remove each element except for the last one in first queue
        while(len(self.q1) > 1):
            self.q2.append(self.q1.pop(0))

        pop_element = self.q1.pop(0)  # element we're gonna return
        # switch queue1 and queue2
        self.q1, self.q2 = self.q2, self.q1
        return pop_element

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if len(self.q1) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
