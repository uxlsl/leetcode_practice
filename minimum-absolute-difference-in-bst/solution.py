# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root is None:
            return 0
        val = 0
        if root and root.left:
            val = min(val, abs(root.val - root.left.val))

        if root and root.right:
            val = min(val, abs(root.val - root.right.val))
        return min(val, self.getMinimumDifference(root.left),
                        self.getMinimumDifference(root.right))
