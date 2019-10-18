class Solution(object):
    def fraction(self, cont):
        """
        :type cont: List[int]
        :rtype: List[int]
        """

        result = [cont[-1], 1]

        for i in cont[::-1][1:]:
            result[0],result[1] = i*result[0]+result[1],result[0]


        return result
