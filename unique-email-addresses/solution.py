# 独特的电子邮件地址
# https://leetcode-cn.com/problems/unique-email-addresses/

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        m = set()
        a_status = 1 # +
        b_status = 2 # @
        for email in emails:
            s = ''
            status = 0
            for i in email:
                if status == b_status:
                    s += i
                else:
                    if status != a_status:
                        if i != '.' and i != '+':
                            s += i
                    if i == '@':
                        if status == a_status:
                            s += '@'
                        status = b_status
                    if i == '+':
                        status = a_status
            m.add(s)
        return len(m)
