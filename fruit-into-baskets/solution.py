# leetcode
# https://leetcode-cn.com/problems/fruit-into-baskets/

# 暴力法


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        # 错误
        from collections import defaultdict

        ret = 0
        count = 0
        # 记录水果数量
        m = defaultdict(int)
        first, second = None, None

        for i in tree:
            count += 1
            if first is None:
                first = i
            elif first != i and second is None:
                second = i
            else:
                if not (i == first or i == second):
                    count -= m[first]
                    del m[first]
                    first, second = second, i
            ret = max(ret, count)
            m[i] += 1

        return ret

    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(len(tree)):
            count = 0
            mem = set()
            for j in range(i, len(tree)):
                if len(mem) < 2:
                    mem.add(tree[j])
                elif tree[j] not in mem:
                    break
                count += 1
            ret = max(ret, count)

        return ret
