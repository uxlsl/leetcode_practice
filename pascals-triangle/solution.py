class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lst = []
        for i in range(1, numRows+1):
            if i == 1:
                row = [1]
            else:
                row = []
                for j in range(i):
                    val = 0
                    if  0 <= j - 1:
                        val = lst[-1][j-1]
                    if j < len(lst[-1]):
                        val += lst[-1][j]
                    row.append(val)
            lst.append(row)
        return lst

