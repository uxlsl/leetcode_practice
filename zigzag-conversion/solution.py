class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        mat = [[] for _ in range(numRows)]
        n = 2*numRows - 2
        for i,c in enumerate(s):
            index = i % n
            if index < numRows:
                mat[index].append(c)
            else:
                mat[numRows-2-(index-numRows)].append(c)
        return ''.join(''.join(i) for i in mat)
