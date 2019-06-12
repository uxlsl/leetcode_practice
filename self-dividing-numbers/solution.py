class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for i in range(left,right+1):
            # 个位,十位,百位等等
            n = i
            while n > 0:
                a = n % 10
                if a and i % a == 0:
                    n = n // 10
                else:
                    break
            else:
                ret.append(i)

        return ret
