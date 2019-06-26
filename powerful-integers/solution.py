class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        import math
        a = int(math.log(bound, x)) if x > 1 else 1
        b = int(math.log(bound, y)) if y > 1 else 1
        ret = set()
        for i in range(a+1):
            for j in range(b+1):
                val = x**i+y**j
                if val <= bound:
                    ret.add(val)

        return list(ret)
