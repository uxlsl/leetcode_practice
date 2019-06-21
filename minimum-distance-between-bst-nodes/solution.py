# leetcode
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
# 解决方法
# 1
# 排序,然后求彼此的差
# 2
# 差最小值发生在父节点和子节点之间

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def walk(self,root):
            if root:
                ret = min(
                    self.ret,
                    root.val - root.left.val if root.left else float("inf"),
                    root.right.val - root.val if root.right else float("inf"),
                )
                walk(self, root.left)
                walk(self, root.right)

        self.ret = float("inf")
        walk(self, root)
        return ret
