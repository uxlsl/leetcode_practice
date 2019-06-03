# https://leetcode-cn.com/problems/flower-planting-with-no-adjacent/
# 有 N 个花园，按从 1 到 N 标记。在每个花园中，你打算种下四种花之一。

# paths[i] = [x, y] 描述了花园 x 到花园 y 的双向路径。

# 另外，没有花园有 3 条以上的路径可以进入或者离开。

# 你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。

# 以数组形式返回选择的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用  1, 2, 3, 4 表示。保证存在答案。



# 示例 1：

# 输入：N = 3, paths = [[1,2],[2,3],[3,1]]
# 输出：[1,2,3]
# 示例 2：

# 输入：N = 4, paths = [[1,2],[3,4]]
# 输出：[1,2,1,2]
# 示例 3：

# 输入：N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# 输出：[1,2,3,4]

class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        # 先种一个花园,然后再看下一个花园能种什么

        garden = {}

        for x,y in paths:
            if x in garden:
                garden[x].add(y)
            else:
                garden[x] = {y}
            x,y = y, x
            if x in garden:
                garden[x].add(y)
            else:
                garden[x] = {y}

        seed = {}
        for k in range(1,N+1):
            seed[k] = {1,2,3,4}

        result = []
        for i in range(1, N+1):
            x = seed[i].pop()
            result.append(x)
            if i in garden:
                for j in garden[i]:
                    if x in seed[j]:
                        seed[j].remove(x)
        return result


