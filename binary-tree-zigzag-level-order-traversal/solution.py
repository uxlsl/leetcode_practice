# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def f(root, lst, level):
            if root:
                if len(lst) < level:
                    lst.append([])
                if (level-1) % 2 == 0:
                    lst[level-1].append(root.val)
                else:
                    lst[level-1].insert(0,root.val)
                f(root.left, lst, level+1)
                f(root.right, lst, level+1)

        ret = []
        f(root, ret, 1)
        return ret
