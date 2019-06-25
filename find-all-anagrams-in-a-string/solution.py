# leetcode
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        A = [0] * 26
        for c in p:
            A[ord(c)-ord('a')] += 1

        B = [0] * 26
        for c in s[:len(p)-1]:
            B[ord(c)-ord('a')] += 1

        ret = []
        for i in range(len(p)-1,len(s)):
            c = s[i]
            B[ord(c)-ord('a')] += 1
            if i - len(p) >= 0:
                c = s[i - len(p)]
                B[ord(c)-ord('a')] -= 1
            if A == B:
                ret.append(i-len(p)+1)

        return ret
