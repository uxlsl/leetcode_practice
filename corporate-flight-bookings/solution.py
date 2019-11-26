class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        # 超时了
        arr = [0] * n

        for book in bookings:
            for i in range(book[0], book[1] + 1):
                arr[i - 1] += book[2]

        return arr
