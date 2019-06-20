# leetcode
# https://leetcode-cn.com/problems/binary-tree-tilt/
# 使用官方解法
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        return self.tilt

    def traverse(self, root):
        if root is None:
            return 0

        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.tilt += abs(left-right)
        return left+right+root.val
