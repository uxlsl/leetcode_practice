"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def f(root, level, mem):
            if root:
                if level in mem:
                    node = mem[level]
                    node.next = root
                mem[level] = root
                f(root.left, level+1, mem)
                f(root.right, level+1, mem)
            return root

        return f(root, 0, {})
