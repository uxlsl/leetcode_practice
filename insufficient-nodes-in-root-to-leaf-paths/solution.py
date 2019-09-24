# leetcode
# 叶节点
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """

        def f(root, val, limit):
            if root:
                cur = root.val + val
                left = f(root.left, cur, limit)
                right = f(root.right, cur, limit)
                if left is None and right is None:
                    if cur >= limit:
                        return root
                    else:
                        return None
                root.left = left
                root.right = right
                return root
            else:
                return None

        return f(root, 0, limit)
