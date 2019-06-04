# 输入：A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# 输出：[8,6,2,4]
# 解释：
# 开始时，数组为 [1,2,3,4]。
# 将 1 加到 A[0] 上之后，数组为 [2,2,3,4]，偶数值之和为 2 + 2 + 4 = 8。
# 将 -3 加到 A[1] 上之后，数组为 [2,-1,3,4]，偶数值之和为 2 + 4 = 6。
# 将 -4 加到 A[0] 上之后，数组为 [-2,-1,3,4]，偶数值之和为 -2 + 4 = 2。
# 将 2 加到 A[3] 上之后，数组为 [-2,-1,3,6]，偶数值之和为 -2 + 6 = 4。

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        results = []
        cur = sum(i for i in A if i % 2 == 0)
        for val,index in queries:
            x = A[index]
            y = x + val
            A[index] = y
            if x % 2 ==0:
                if y % 2 == 0:
                    cur += val
                else:
                    cur -=  x
            elif y % 2 == 0:
                cur += y
            results.append(cur)

        return results
