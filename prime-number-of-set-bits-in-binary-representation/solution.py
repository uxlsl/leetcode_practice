# leetcode
# https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation/

# 解法:
# 1: 计算1数量
# 2: 素数

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def isPrime(n) :
	    # Corner cases
            if (n <= 1):
                return False
            if (n <= 3) :
                return True

	    # This is checked so that we can skip
	    # middle five numbers in below loop
            if (n % 2 == 0 or n % 3 == 0) :
                return False
            i = 5
            while(i * i <= n) :
                if (n % i == 0 or n % (i + 2) == 0) :
                    return False
                i = i + 6
            return True

        def count_bit(n):
            count = 0
            while n&0xffffffff != 0:
                n = n & (n-1)
                count += 1

            return count

        total = 0
        for i in range(L,R+1):
            if isPrime(count_bit(i)):
                total += 1

        return total
