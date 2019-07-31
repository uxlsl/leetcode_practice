# leetcode
# https://leetcode-cn.com/problems/all-possible-full-binary-trees/
# 递归解决
# 类似格雷码
# Definition for a binary tree node.

import copy
import functools


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        @functools.lru_cache(None)
        def f(N):
            root = TreeNode(0)
            if N == 1:
                return [root]
            if N % 2 == 0:
                return []
            ret = []
            for i in range(1, N, 2):
                left = f(i)
                right = f(N-1-i)
                for l in left:
                    for r in right:
                        root.left = l
                        root.right = r
                        ret.append(copy.deepcopy(root))
            return ret
        return f(N)
