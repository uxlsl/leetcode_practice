class MyCalendar(object):
    def __init__(self):
        self._data = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s, e in self._data:
            if not (end <= s or e <= start):
                return False

        self._data.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
