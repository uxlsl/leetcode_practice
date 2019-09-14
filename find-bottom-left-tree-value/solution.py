# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def f(root,vals,level):
            if root:
                if len(vals) < level:
                    vals.append(root.val)
                f(root.left, vals, level+1)
                f(root.right, vals, level+1)

        vals = []
        f(root,vals,1)
        return vals[-1]
