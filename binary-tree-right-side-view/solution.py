# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def LevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def f(root, lst, level):
            if root:
                if len(lst) < level:
                    lst.append([])
                lst[level-1].append(root.val)
                f(root.left, lst, level+1)
                f(root.right, lst, level+1)

        ret = []
        f(root, ret, 1)
        return ret

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return [a[-1]
                for a in self.LevelOrder(root)]
