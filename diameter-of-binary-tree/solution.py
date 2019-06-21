# leetcode
# https://leetcode-cn.com/problems/diameter-of-binary-tree/
# 解法
# 求深度

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 算每一个节点的二边深度之和
        # 相当于二边深度相加

        def dfs(node):
            "求深度"
            if node is None:
                return 0
            else:
                return max(
                    dfs(node.left) + 1 if node.left else 0,
                    dfs(node.right) + 1 if node.right else 0,
                )

        def dia(node):
            if node:
                return (dfs(node.left) + 1 if node.left else 0) + (
                    dfs(node.right) + 1 if node.right else 0
                )
            else:
                return 0

        def maxDia(root):
            if root:
                return max(dia(root), maxDia(root.left), maxDia(root.right))
            return 0

        return maxDia(root)
