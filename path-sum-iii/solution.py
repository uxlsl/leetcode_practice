import collections

class Solution(object):
    def _pathSum(self, root, cur, sum, record):
        if root is None:
            return 0
        cur += root.val
        result = record[cur - sum]
        record[cur] += 1
        result += self._pathSum(root.left, cur, sum, record)
        result += self._pathSum(root.right, cur, sum, record)
        record[cur] -= 1
        if record[cur] == 0:
            del record[cur]
        return result


    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        record = collections.defaultdict(int)
        record[0] = 1
        return self._pathSum(root, 0, sum, record)
