# leetcode
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 节点相交
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def f(root,p, path):
            if root.val == p.val:
                return True
            for node in [root.left, root.right]:
                if node:
                    path.append(node)
                    if f(node, p, path):
                        return True
                    path.pop()
            return False

        p_path = [root]
        f(root, p, p_path)
        q_path = [root]
        f(root, q, q_path)
        for i,j in zip(p_path, q_path):
            if i.val != j.val:
                break
            last = i
        return last
