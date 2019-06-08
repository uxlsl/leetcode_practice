class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        a = list(range(2,n+1))

        i = 0
        while True:
            x = a[i]
            if x * x > a[-1]:
                return len(a)

            b = a[:i+1]
            for j in a[i+1:]:
                if j % x != 0:
                    b.append(j)
            a = b
            i += 1
