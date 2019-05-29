class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = -float('inf')
        neg_cur = None
        pos_cur = None
        for i in nums:
            if i == 0:
                neg_cur = None
                pos_cur = None
                result = max(result, 0)
                continue
            elif i > 0:
                if pos_cur:
                    pos_cur *= i
                else:
                    pos_cur = i
                if neg_cur:
                    neg_cur *= i
            else:
                if neg_cur:
                    tmp = pos_cur
                    pos_cur = neg_cur * i
                    if tmp:
                        neg_cur = tmp * i
                    else:
                        neg_cur = i
                else:
                    if pos_cur:
                        neg_cur = pos_cur * i
                        pos_cur = None
                    else:
                        neg_cur = i
            if pos_cur and pos_cur > result:
                result = pos_cur
            if neg_cur and neg_cur > result:
                result = neg_cur
        return result
