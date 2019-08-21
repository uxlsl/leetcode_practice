# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def f(root, sum, path, result):
            if root is None:
                return
            path.append(root.val)
            if sum - root.val == 0 and root.left is None and  root.right is None:
                result.append(list(path))

            f(root.left, sum - root.val, path, result)
            f(root.right, sum - root.val, path, result)
            path.pop()

        result = []
        path = []
        f(root, sum, path, result)
        return result

