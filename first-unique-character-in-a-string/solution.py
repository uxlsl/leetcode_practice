class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = set()
        b = list() # 侯选
        c = dict()

        for num, i in enumerate(s):
            if i not in a:
                a.add(i)
                b.append(i)
                c[i] = num
            else:
                try:
                    b.remove(i)
                except ValueError:
                    pass
        try:
            return c[b[0]]
        except IndexError:
            return -1
