class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        min_num = min(nums)
        s = set(nums)
        longest = 0
        while s:
            cur = 1
            a = s.pop()
            for i in xrange(a-1,min_num,-1):
                if i not in s:
                    break
                s.remove(i)
                cur += 1
            for i in xrange(a+1,max_num,):
                if i not in s:
                    break
                s.remove(i)
                cur += 1
            longest = max(cur, longest)
        return longest

