class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        val = 0
        for _ in range(32):
            val <<= 1
            val |= n & 0x1
            n >>=1
        return val
