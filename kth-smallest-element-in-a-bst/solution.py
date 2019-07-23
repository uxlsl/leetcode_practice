# leetcode
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
# 解决方法
# 1. 简单排序,然后输出第K小的元素

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def f(root,lst):
            if root:
                f(root.left)
                # 这里可以改为计数
                lst.append(root.val)
                f(root.right)
        lst = []
        f(root,lst)
        return lst[k-1]
