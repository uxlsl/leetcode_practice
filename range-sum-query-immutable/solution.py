class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        val = 0
        cal = [val]
        for i in nums:
            val += i
            cal.append(val)
        self.cal = cal


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        try:
            return self.cal[j+1] - self.cal[i]
        except IndexError:
            return 0



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
