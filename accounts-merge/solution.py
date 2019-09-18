# leetcode
# https://leetcode-cn.com/problems/accounts-merge/

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def f(emails, email, visited, user):
            if email in visited:
                return
            visited.add(email)
            user.append(email)
            for i in emails[email]:
                if len(user) == 1:
                    user.insert(0, i[0])
                for j in i[1:]:
                    f(emails, j, visited, user)


        from collections import defaultdict

        emails = defaultdict(list)

        for i in accounts:
            for email in i[1:]:
                emails[email].append(i)

        ret = []
        visited = set()
        for email in emails.keys():
            if email not in visited:
                user = []
                f(emails, email,visited, user)
                user = [user[0]] + sorted(user[1:])
                ret.append(user)

        return ret
