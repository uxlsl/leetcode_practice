class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def same(p, q):
            if p is None and q is not None:
                return False
            if p is not None and q is None:
                return False
            if p is None and q is None:
                return True
            if p.val == q.val:
                return same(p.left, q.right) \
                        and same(p.right, q.left)
            else:
                return False
        if root is None:
            return True
        return same(root.left, root.right)
