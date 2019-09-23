# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        val = None

        def to_c(x):
            return chr(ord('a') + x)

        def f(root,cur):
            nonlocal val
            if root:
                if root.left is None and root.right is None:
                    x = to_c(root.val) + cur
                    if val is None:
                        val = x
                    elif val > x:
                        val = x
                else:
                    f(root.left, x)
                    f(root.right, x)

        f(root, '')
        return val
