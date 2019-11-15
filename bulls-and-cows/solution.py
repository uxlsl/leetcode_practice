class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        from collections import defaultdict

        A = 0
        a1 = defaultdict(int)
        a2 = defaultdict(int)
        for i, j in zip(secret, guess):
            if i == j:
                A += 1
            else:
                a1[i] += 1
                a2[j] += 1

        B = 0

        for i in a1.keys() & a2.keys():
            B += min(a1[i], a2[i])

        return "{}A{}B".format(A, B)
