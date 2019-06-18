class RecentCounter(object):

    def __init__(self):
        from collections import deque
        self.queue = deque()


    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while True:
            if len(self.queue) == 0:
                break
            a = self.queue.popleft()
            if a >= t - 3000:
                self.queue.appendleft(a)
                break
        self.queue.append(t)
        return len(self.queue)




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
