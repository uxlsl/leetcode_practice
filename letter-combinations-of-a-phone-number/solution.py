class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = {
                '2':'abc',
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz',
            }
        if digits == '':
            return []
        results = list(m[digits[0]])
        for c in digits[1:]:
            if results:
                tmp = []
                for x in m[c]:
                    tmp.extend([i+x for i in results])
                results = tmp
        return results

