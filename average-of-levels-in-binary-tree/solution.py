class Solution(object):
    def _averageOfLevels(self, root, lst, depth):
        if root is None:
            return
        if len(lst) < depth+1:
            lst.append([0,0])
        lst[depth][0] += root.val
        lst[depth][1] += 1
        self._averageOfLevels(root.left, lst, depth+1)
        self._averageOfLevels(root.right, lst, depth+1)

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        lst = []
        self._averageOfLevels(root, lst, 0)
        return [float(x)/y for x,y in lst]
