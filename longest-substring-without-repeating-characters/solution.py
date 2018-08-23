class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = {}
        max_l = cur = 0
        for i,v in enumerate(s):
            if v in record:
                j = record[v]
                for x in range(i-cur, record[v]+1):
                    del record[s[x]]
                cur = i - j
            else:
                cur += 1
            record[v]=i
            max_l = max(max_l, cur)
        return max_l
