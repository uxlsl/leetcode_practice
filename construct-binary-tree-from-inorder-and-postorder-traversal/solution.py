# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def f(inorder, postorder, start, end):
            if postorder and start <= end:
                v = postorder.pop()
                node = TreeNode(v)
                i = inorder.index(v)
                node.right = f(inorder, postorder, i + 1, end)
                node.left = f(inorder, postorder, start, i - 1)
                return node
            return None
        return f(inorder, postorder, 0, len(inorder) - 1)
