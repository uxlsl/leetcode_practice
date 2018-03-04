# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _findTarget(self, root, k, lookup):
        if root is None:
            return False
        if k - root.val in lookup:
            return True
        else:
            lookup.add(root.val)
            return self._findTarget(root.left, k, lookup)\
                    or self._findTarget(root.right, k, lookup)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        return self._findTarget(root, k, set())
