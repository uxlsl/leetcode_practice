"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        def f(n,lst):
            if n:

                for child in n.children:
                    f(child,lst)
                lst.append(n.val)

            return lst

        return f(root, [])
