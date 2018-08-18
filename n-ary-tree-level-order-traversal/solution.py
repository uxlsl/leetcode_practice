"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        lst = []
        self.f(root, lst, 0)
        return lst
        
    def f(self, root, lst, level):
        if root:
            if len(lst) < level+1:
                lst.append([])
            lst[level].append(root.val)
            if root.children:
                for node in root.children:
                    self.f(node, lst, level+1)
