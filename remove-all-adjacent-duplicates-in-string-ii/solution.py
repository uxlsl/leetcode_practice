# leetcode
# https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string-ii/


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []

        for c in s:
            if stack:
                top = stack[-1]
                if top[0] == c:
                    if top[1] + 1 == k:
                        stack.pop()
                    else:
                        top[1] += 1
                else:
                    stack.append([c, 1])
            else:
                stack.append([c,1])

        return ''.join(
                i[0]*i[1]
                for i in stack)
