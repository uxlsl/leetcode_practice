# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mem = {}
        def f(root):
            if root in mem:
                return mem[root]
            if root:
                val = root.val
                if root.left:
                    val += f(root.left.left)
                    val += f(root.left.right)

                if root.right:
                    val += f(root.right.left)
                    val += f(root.right.right)

                ret = max(val, f(root.left) + f(root.right))
                mem[root] = ret
                return ret
            else:
                return 0

        return f(root)
