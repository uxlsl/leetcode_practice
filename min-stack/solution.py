class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.B = []

    @property
    def min(self):
        try:
            return self.stack[self.B[-1]]
        except IndexError as e:
            return None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min is None or self.min > x:
            self.B.append(len(self.stack)-1)

    def pop(self):
        """
        :rtype: void
        """
        if self.B and len(self.stack) - 1 == self.B[-1]:
            self.B.pop()
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        try:
            return self.stack[-1]
        except:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
