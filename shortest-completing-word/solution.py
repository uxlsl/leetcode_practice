class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate = [c for c in licensePlate.lower() if c.isalpha()]
        min_word = None
        for word in words:
            m = {}

            for c in word:
                if c in m:
                    m[c] += 1
                else:
                    m[c] = 1

            for c in licensePlate:
                if c not in m or m[c] - 1 < 0:
                    break
                m[c] -= 1
            else:
                if min_word is None or len(min_word) > len(word):
                    min_word = word

        return min_word
