# leetcode
# https://leetcode-cn.com/problems/add-one-row-to-tree/
# 添加规则：给定一个深度值 d （正整数），针对深度为 d-1 层的每一非空节点 N，为 N 创建两个值为 v 的左子树和右子树。

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """

        def f(root, v, d):
            if root:
                if d == 1:
                    l,r = root.left, root.right
                    root.left = TreeNode(v)
                    root.right = TreeNode(v)
                    root.left.left = l
                    root.right.right = r
                    return root
                f(root.left, v, d-1)
                f(root.right, v, d-1)
                return root

        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        return f(root, v, d-1)
