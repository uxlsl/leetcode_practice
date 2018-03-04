class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        x = y = None

        if root.left:
            x = self.maxDepth(root.left) + 1

        if root.right:
            y = self.maxDepth(root.right) + 1

        if x is None or y is None:
            return x or y
        else:
            return max(x, y)
