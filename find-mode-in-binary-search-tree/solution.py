# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import Counter
        def f(root, lst):
            if root:
                lst.append(root.val)
                f(root.left,lst)
                f(root.right,lst)

        lst = []
        f(root, lst)
        if lst:
            c = Counter(lst)
            a = c.most_common()[0][0]
            return [i for i in c.most_common() if i[1] == a[1]]
        return []
