class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        from collections import defaultdict
        m = defaultdict(int)

        for c in text:
            m[c] += 1

        count = 0
        while True:
            for c in "balloon":
                if c not in m or m[c] - 1 < 0:
                    return count
                m[c] -= 1
            count += 1

