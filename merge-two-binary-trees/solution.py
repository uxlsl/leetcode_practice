class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        def merge(t1, t2, n):
            print(id(t1), id(t2), id(n))
            if t1 is None and t2 is None:
                return

            if t1 is not None and t2 is None:
                return

            if t1 is None and t2 is not None:
                return

            n.val = t1.val + t2.val
            if n.left:
                merge(t1.left, t2.left, n.left)

            n.left = t1.left or t2.left

            if n.right:
                if id(t1.right) == id(t2.right):
                    raise ValueError()
                merge(t1.right, t2.right, n.right)

            n.right = t1.right or t2.right

        root = t1 or t2
        if root:
            merge(t1, t2, root)
        return root
