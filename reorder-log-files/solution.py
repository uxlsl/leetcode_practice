# leetcode
# https://leetcode-cn.com/problems/reorder-log-files/
# 注意 split的参数使用

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        l1 = []
        l2 = []

        for log in logs:
            if log.split()[1].isalpha():
                l1.append(log)
            else:
                l2.append(log)

        return sorted(l1, key=lambda x:(x.split()[1:],x.split()[0])) + l2

