class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lst = [str(i) for i in range(1,n+1)]
        return [int(i) for i in sorted(lst)]
