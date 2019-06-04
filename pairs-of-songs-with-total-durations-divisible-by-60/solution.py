# 二数求模
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        count = 0
        index = [0]*60
        for n in time:
            count += index[(60 - n % 60) % 60];
            index[n % 60] +=1
        return count
