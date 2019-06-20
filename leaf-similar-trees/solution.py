# leetcode
# https://leetcode-cn.com/problems/leaf-similar-trees/submissions/
# 解法,收集叶子,进行对比

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def f(root, list1):
            if root is not None:
                if root.left is None and root.right is None:
                    list1.append(root.val)
                else:
                    f(root.left, list1)
                    f(root.right, list1)
            return list1
        return f(root1, []) == f(root2, [])
