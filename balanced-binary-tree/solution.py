class NotBalance(Exception):
    pass

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(p, q):
            if p is not None:
                l = check(p.left, p.right)
            else:
                l = 0
            if q is not None:
                r = check(q.left, q.right)
            else:
                r = 0
            if abs(l -r ) > 1:
                raise NotBalance
            return max(l+1, r+1)

        if root is None:
            return True
        try:
            check(root.left, root.right)
            return True
        except NotBalance:
            return False
