class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split()
        i = 0
        ret = []
        while i < len(words) -2:
            if words[i] == first and words[i+1] == second:
                ret.append(words[i+2])
            i += 1
        return ret

