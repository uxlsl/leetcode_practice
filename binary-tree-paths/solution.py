class Solution(object):
    def fmt(self, cur, node):
        if cur == '':
            return '{}'.format(node.val)
        else:
            return '{}->{}'.format(cur, node.val)

    def _binaryTreePaths(self, root, cur, lst):
        if root is None:
            return
        if root.left is None and root.right is None:
            lst.append(self.fmt(cur, root))
            return
        self._binaryTreePaths(root.left, self.fmt(cur, root), lst)
        self._binaryTreePaths(root.right, self.fmt(cur, root), lst)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        lst = []
        self._binaryTreePaths(root, '', lst)
        return lst

