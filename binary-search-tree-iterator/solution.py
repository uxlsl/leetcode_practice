# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def f(node, lst):
    if node:
        f(node.left, lst)
        lst.append(node.val)
        f(node.right, lst)


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self._data = []
        f(root, self._data)
        self._data = self._data[::-1]

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self._data.pop()


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self._data) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
