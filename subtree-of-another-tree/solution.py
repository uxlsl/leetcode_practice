# leetcode
# https://leetcode-cn.com/problems/subtree-of-another-tree/
# 解法:同一树加遍历节点
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def same(s,t):
            if s is None and t is None:
                return True
            elif s and t and s.val == t.val:
                return same(s.left, t.left) and same(s.right,t.right)
            else:
                return False

        def walk(s, t):
            return same(s,t) or walk(s.left, t) or walk(s.right, t)

        return walk(s,t)
