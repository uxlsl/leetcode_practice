class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        total = sum(A)
        if total % 3 != 0:
            return False

        count = 0
        s = 0
        for i in A:
            s += i
            if s == (total // 3 * (count + 1)):
                count += 1
                if count == 3:
                    return True
        else:
            return False
