class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        result = a ^ b
        carray = (a & b) << 1
        if carray!=0:
            return  self.getSum(result,carray)
        return result
