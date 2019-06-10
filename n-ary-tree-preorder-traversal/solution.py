"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        def f(n,lst):
            if n:
                lst.append(n.val)
                for child in self.children:
                    f(child)
            return lst

        return f(n, [])
