# leetcode
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
# 如果使用空间，会比较容易
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

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root
