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

        pq = root
        while True:
            if pq.val < p.val and pq.val < q.val:
                pq = pq.left
            elif pq.val > p.val and pq.val > q.val:
                pq = pq.right
            elif ((pq.val < p.val and pq.val > q.val)
                 or (pq.val > p.val and pq.val < q.val)):
                return pq
            elif pq.val == p.val:
                return p
            elif pq.val == q.val:
                return q
