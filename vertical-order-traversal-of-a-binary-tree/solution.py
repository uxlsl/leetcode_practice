# leetcode
# 如果两个结点位置相同，则首先报告的结点值较小。

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def f(root, dic, x, y):
            if root:
                dic[x].append((y, root.val))
                f(root.left, dic, x - 1, y - 1)
                f(root.right, dic, x + 1, y - 1)

        dic = defaultdict(list)
        f(root, dic, 0, 0)
        lst = sorted(dic.items(), key=lambda x: x[0])

        return [
            [i[1] for i in sorted(x, key=lambda x: (x[0], -x[1]), reverse=True)]
            for _, x in lst
        ]
