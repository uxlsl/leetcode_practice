class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ret = [0] * num_people
        x = 1
        while True:
            for i in range(num_people):
                if candies <= 0:
                    return ret
                ret[i] += min(x, candies)
                candies -= min(x, candies)
                x += 1
