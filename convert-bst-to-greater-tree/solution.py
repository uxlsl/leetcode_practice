# leetcode
# https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
# 找规律
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def f(node, val):
            if node is not None:
                node.val += f(node.right, val)
                return f(node.left, node.val)
            else:
                return val

        f(root, 0)
        return root
