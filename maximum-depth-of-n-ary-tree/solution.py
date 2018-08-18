"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root:
            if root.children:
                return 1+max(self.maxDepth(n) for n in root.children)
            else:
                return 1
        return 0
