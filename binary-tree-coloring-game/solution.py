# leetcode
# 总节点数
# 三个方向的节点数对比
# 一个方向的节点大于二个方向的节点数，着色成功

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """

        def f(root):
            if root:
                return 1 + f(root.left) + f(root.right)
            return 0

        def f_x(root, x):
            if root:
                if root.val == x:
                    return root
                return f_x(root.left, x) or f_x(root.right, x)
            return None

        total = f(root)
        x_node = f_x(root, x)

        x_left_total = f(x_node.left)
        x_right_total = f(x_node.right)
        x_p_total = total - x_left_total - x_right_total - 1

        return (
                x_p_total > x_left_total + x_right_total + 1 or
                x_left_total > x_right_total + x_p_total + 1 or
                x_right_total > x_left_total + x_p_total + 1)

