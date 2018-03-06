class Solution(object):
    def _pathSum(self, root, sum, record):
        if root is None:
            return
        record[0].append(record[0][-1]+root.val)
        if record[0][-1] - sum in record[0]:
            record[1] += 1
        self._pathSum(root.left, sum, record)
        self._pathSum(root.right, sum, record)
        record[0].pop()


    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        record = [[0], 0]
        self._pathSum(root, sum, record)
        return record[1]
