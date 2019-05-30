class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        seen = set()
        for word in words:
            s = ''
            for c in word:
                s += m[ord(c) - ord('a')]
            seen.add(s)
        return len(seen)

