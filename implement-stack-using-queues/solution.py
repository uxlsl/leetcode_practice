class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
	self.data = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.data.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.data.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.data[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.data) == 0
