class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''

        s = '{}'.format(t.val)

        if t.left is None and t.right:
            s += '()' + '(' + self.tree2str(t.right) + ')'
            return s

        if t.left:
            s += '({})'.format(self.tree2str(t.left))

        if t.right:
            s += '({})'.format(self.tree2str(t.right))

        return s
