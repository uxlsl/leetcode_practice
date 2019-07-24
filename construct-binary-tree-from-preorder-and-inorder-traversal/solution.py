# leetcode
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def f(preorder, inorder, start, end):
            """
            start, end 针对中序
            """
            if preorder and start <= end:
                v = preorder.pop(0)
                node = TreeNode(v)
                i = inorder.index(v)
                node.left = f(preorder, inorder, start, i - 1)
                node.right = f(preorder, inorder, i + 1, end)
                return node
            return None

        return f(preorder, inorder, 0, len(inorder) - 1)
