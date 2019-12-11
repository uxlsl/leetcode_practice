# leetcode
# https://leetcode-cn.com/problems/fruit-into-baskets/

# 暴力法
import collections
import itertools


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        # 错误解法
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
        # 超时算法
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

    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(tree) == 0:
            return 0

        l = [tree[0]]
        count = 1
        ret = 1
        p1 = 0

        for p in range(1, len(tree)):
            if tree[p] in l:
                l.remove(tree[p])
            l.append(tree[p])
            count += 1
            if len(l) > 2:
                l.pop(0)
                while True:
                    if tree[p1] == l[0]:
                        break
                    count -= 1
                    p1 += 1

            print(l,count)
            ret = max(ret, count)

        return ret

    def totalFruit(self, tree):
        blocks = [(k, len(list(v)))
                  for k, v in itertools.groupby(tree)]
        ans = i = 0
        while i < len(blocks):
            # We'll start our scan at block[i].
            # types : the different values of tree[i] seen
            # weight : the total number of trees represented
            #          by blocks under consideration
            types, weight = set(), 0

            # For each block from i and going forward,
            for j in range(i, len(blocks)):
                # Add each block to consideration
                types.add(blocks[j][0])
                weight += blocks[j][1]

                # If we have 3 types, this is not a legal subarray
                if len(types) >= 3:
                    i = j-1
                    break

                ans = max(ans, weight)

            # If we go to the last block, then stop
            else:
                break

        return ans


    def totalFruit(self, tree):
        ans = 0
        i = 0
        count = collections.defaultdict(int)
        for j,v in enumerate(tree):
            count[v] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i+= 1
            ans = max(ans, j-i+1)

        return ans
