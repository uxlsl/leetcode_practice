class Solution(object):
    def find(self, node, n, path):
        if node is None:
            return False
        if node == n:
            return True
        for i in [node.left, node.right]:
            if i:
                path.append(n)
                if self.find(i, n, path):
                    return True
                else:
                    path.pop()
        return False

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None or q is None:
            return None

        l1 = []
        self.find(root, p, l1)
        if q in l1:
            return q

        l2 = []
        self.find(root, q, l2)
        if p in l2:
            return q

        for i in range(min(len(l1), len(l2))):
            if l1[i] != l2[i]:
                return l1[i-1]
        else:
            return l1[i]

