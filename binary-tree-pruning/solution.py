# leetcode
# https://leetcode-cn.com/problems/binary-tree-pruning/
# 解决方法
# 如果子树全为0就去掉
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def f(root):
            if root is None:
                return True
            if f(root.left):
                root.left = None
            if f(root.right):
                root.right = None
            if root.left is None and root.right is None:
                if root.val == 0:
                    return True
                else:
                    return False
            return False
        f(root)
        return root
