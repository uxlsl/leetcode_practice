class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """

        count = 0
        for i, j in zip(guess, answer):
            if i == j:
                count += 1
        return count
