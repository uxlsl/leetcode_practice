class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        def merge(t1, t2, n):

            if t1 is None and t2 is None:
                return

            if t1 is not None and t2 is None:
                n.val = t1.val
                return

            if t1 is None and t2 is not None:
                n.val = t2.val
                return

            n.val = t1.val + t2.val
            n.left = t1.left or t2.left
            if n.left:
                merge(t1.left, t2.left, n.left)

            n.right = t1.right or t2.right
            if n.right:
                merge(t1.right, t2.right, n.right)

        root = t1 or t2
        if root:
            merge(t1, t2, root)
        return root
