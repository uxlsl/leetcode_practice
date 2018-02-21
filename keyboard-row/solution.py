class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lines = [
                set('qwertyuiop'),
                set('asdfghjkl'),
                set('zxcvbnm'),]
        lst = []
        for word in words:
            for line in lines:
                if set(word.lower()) <= line:
                    lst.append(word)
        return lst
