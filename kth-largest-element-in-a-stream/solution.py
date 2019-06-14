class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.data = sorted(nums, reverse=True)[:k]


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        data = self.data

        if len(data) < self.k:
            data.append(val)
        else:
            if data[-1] < val:
                data[-1] = val


        i = len(data) - 1

        while i > 0 and data[i-1] < data[i]:
            data[i-1],data[i] = data[i],data[i-1]
            i -= 1
        return data[-1]
