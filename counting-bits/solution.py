class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 可优化 
        results = []

        for i in range(num+1):
            count = 0
            while i > 0:
                if i < len(results):
                    count += results[i]
                    break
                count += 1
                i = i &(i-1)
            results.append(count)
        return results
