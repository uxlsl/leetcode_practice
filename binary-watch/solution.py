import itertools

class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        lst = []
        for i in itertools.combinations(range(10), num):
            val = 0

            for j in i:
                val |= (1<<j)

            hour = (val >> 6) & 0xf
            if hour > 11:
                continue
            minute = val & 0x3f
            if minute > 59:
                continue
            x = '{}:{:02}'.format(hour, minute)
            lst.append(x)
        return lst
