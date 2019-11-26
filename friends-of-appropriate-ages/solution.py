class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = 0
        for a in range(len(ages)):
            for b in range(len(ages)):
                if a == b:
                    continue
                if ages[b] <= 0.5*ages[a] + 7 or ages[b] > ages[a] or (ages[b] > 100 and ages[a] < 100):
                    continue
                count += 1

        return count
