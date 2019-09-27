# leetcode
# 和计算完全二叉树的差不多
# 求最大深夜
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def get_height(root):
            if root:
                return max(get_height(root.left) + 1, get_height(root.right) + 1)
            return 0

        h = get_height(root)

        layer = [root]

        for _ in range(h-2):
            tmp = []
            for i in layer:
                for j in [i.left, i.right]:
                    if j is None:
                        return False
                    tmp.append(j)

            layer = tmp

        lst = []

        for i in layer:
            for j in [i.left, i.right]:
                if j and lst and lst[-1] is None:
                    return False
                lst.append(j)
        return True
