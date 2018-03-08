class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if p.val < root.val and q.val < root.val:
            x = self.lowestCommonAncestor(root.left,p,q)
            if x:
                return x
        if p.val > root.val and q.val > root.val:
            y = self.lowestCommonAncestor(root.right,p,q)
            if y:
                return y
        if p.val <= root.val <= q.val:
            return root
        if q.val <= root.val <= p.val:
            return root
