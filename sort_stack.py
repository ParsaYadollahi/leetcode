'''
    CTCI 3.5
'''


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.temp_stack = []
        self.sorted_stack = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        while(self.sorted_stack and self.sorted_stack[-1] < x):
            self.temp_stack.append(self.sorted_stack.pop())

        self.sorted_stack.append(x)
        while (self.temp_stack):
            self.sorted_stack.append(self.temp_stack.pop())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # remove each element except for the last one in first queue
        return self.sorted_stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.sorted_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if len(self.sorted_stack) == 0 else False


stack = MyStack()
stack.push(4)
stack.push(3)
stack.push(1)
stack.push(2)
stack.push(85)

print(stack.sorted_stack)
