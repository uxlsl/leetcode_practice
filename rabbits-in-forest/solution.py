class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if len(answers) == 0:
            return 0

        m = {}

        for i in answers:
            if i not in m:
                m[i] = 0
            m[i] += 1

        count = 0
        for k, v in m.items():
            while v > 0:
                count += k + 1
                v -= k + 1

        return count
