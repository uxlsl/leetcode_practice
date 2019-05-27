import heapq

class MaxHeap(object):
    def __init__(self, x):
        self.heap = [-e for e in x]
        heapq.heapify(self.heap)
    def push(self, value):
        heapq.heappush(self.heap, -value)
    def pop(self):
        return -heapq.heappop(self.heap)

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        heap = MaxHeap(stones)
        while len(heap.heap) >= 2:
            a = heap.pop()
            b = heap.pop()
            c = a - b
            if c > 0:
                heap.push(c)
        if len(heap.heap) == 1:
            return -heap.heap[0]
        else:
            return 0
