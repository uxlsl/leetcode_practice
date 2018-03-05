class Solution(object):
    def _levelOrderBottom(self, root, lst, depth):
        if root is None:
            return
        if len(lst) < depth:
            lst.insert(0, [])
        lst[-depth].append(root.val)
        self._levelOrderBottom(root.left, lst, depth+1)
        self._levelOrderBottom(root.right, lst, depth+1)

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lst = []
        self._levelOrderBottom(root, lst, 1)
        return lst

