# leetcode
# https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/

# 提示
# 数组第一个是节点

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """

        def find(array,i,j,v):
            "没有返回-1"

            for x in range(i,j+1):
                if array[x] > v:
                    return x
            return -1

        def build(array,i,j):
            if i > j:
                return
            root = TreeNode(preorder[i])
            m = find(array, i+1,j, array[i])
            if m > 0:
                root.left = build(array, i+1, m-1)
                root.right = build(array, m, j)
            else:
                root.left = build(array, i+1, j)
            return root

        return build(preorder, 0, len(preorder)-1)
