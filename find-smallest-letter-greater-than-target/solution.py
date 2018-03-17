class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if len(letters) == 0:
            return None
        c = letters[0]
        if c > target:
            return c
        for i in letters[1:]:
            if i > target:
                return i
        return c
