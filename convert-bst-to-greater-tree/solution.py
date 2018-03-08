class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def make(root, lst):
            if root is None:
                return
            if root.left:
                lst.append(root.left)
                make(root.left, lst)
            lst.append(root)
            if root.right:
                lst.append(root.right)
                make(root.right, lst)
        lst = []
        make(root, lst)
        lst = sorted(lst, key=lambda x:x.val, reverse=True)
        total = 0
        for i in lst:
            total += i.val
            i.val = total
        return root

