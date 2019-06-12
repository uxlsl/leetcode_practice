class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()

        for i in range(len(words)):
            a = words[i][0].lower()
            if a in ('a', 'e', 'i', 'o', 'u'):
                words[i] += 'ma'
            else:
                words[i] = words[i][1:] + words[i][0] + 'ma'

            words[i] += "a"*(i+1)

        return ' '.join(words)
