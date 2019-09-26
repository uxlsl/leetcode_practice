# Definition for a binary tree node.
import copy
import functools

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        @functools.lru_cache(None)
        def f(start, end):
            """
            start,end 实边界
            """
            # 只有一种可能
            if end == start:
                return [TreeNode(start)]
            if end < start:
                return [None]
            ret = []
            for i in range(start, end + 1):
                root = TreeNode(i)
                for x in f(start, i -1):
                    for y in f(i+1, end):
                        root.left = x
                        root.right = y
                        ret.append(copy.deepcopy(root))
            return ret

        return f(1, n)
