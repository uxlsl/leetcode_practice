import heapq

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def f(node, vals):
            if node is None:
                return
            vals.append(node.val)
            f(node.left,vals)
            f(node.right,vals)
        vals = []
        f(root, vals)
        if vals < 2:
            return -1
        vals = heapq.nsmallest(2, vals)
        return vals[1]
