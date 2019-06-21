# leetcode
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
# 解决方法
# 1
# 排序,然后求彼此的差
# 2
# 中序打印,就是排序结果,利用了python3 yield from

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def walk(self,root):
        if root:
            yield from self.walk(root.left)
            yield root.val
            yield from self.walk(root.right)

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        ret = float('inf')
        i = self.walk(root)
        pre = next(i) # 最少二个

        for v in i:
            if v - pre < ret:
                ret = v - pre
            pre = v

        return ret
