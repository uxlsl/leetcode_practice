# https://coolshell.cn/articles/3738.html

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




class Solution:
    def countPrimes(self, n: int) -> int:
        l = [i for i in range(n)]
        for j in range(2, n):
            if l[j] != 0:
                k = 2
                while k * j < n:
                    l[k * j] = 0
                    k += 1
        count = 0
        for n in l:
            if n !=0 and n!=1:
                count += 1
        return count
