# leetcode
# 重建

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        def f(root, key):
            if root is None:
                return
            if root.val != key:
                if root.val < key:
                    root.right = f(root.right, key)
                else:
                    root.left = f(root.left, key)
                return root
            else:
                if root.right is not None:
                    root.val, root.right.val = root.right.val, root.val
                    root.right = f(root.right, key)
                    return root
                else:
                    if root.left is not None:
                        root.val, root.left.val = root.left.val, root.val
                        root.left = f(root.left, key)
                        return root

        return f(root, key)



class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        if not root: return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if  root.left is None or  root.right is None:
                root = root.left if root.left else root.right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)

        return root
