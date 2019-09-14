# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        def f(root, level):
            if root:
                if len(ret) < level:
                    ret.append(float('-inf'))
                ret[level] = max(ret[level], root.val)
                f(root.left, level+1)
                f(root.right, level+1)

        f(root, 1)
        return ret
