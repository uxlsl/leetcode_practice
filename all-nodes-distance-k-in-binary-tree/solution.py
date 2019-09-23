# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # 求从根节点到指定节点的路径
        def find_node(root, target, path):
            nonlocal find,node_path
            if root and not find :
                if root is target:
                    find = True
                    node_path = list(path)
                    return
                path.append(root)
                find_node(root.left, target, path)
                find_node(root.right, target, path)
                path.pop()

        # 求一个节点下距离的值
        def find_val(root, k, vals):
            if root:
                if k == 0:
                    vals.append(root.val)
                find_val(root.left, k-1, vals)
                find_val(root.right, k-1, vals)

        find = False
        node_path = None
        vals = []
        find_node(root, target, [])
        node_path = list(node_path[::-1])

        l = min(len(node_path), K)

        for i in range(l):
            if i > 0:
                if node_path[i].left == node_path[i-1]:
                    find_val(node_path[i].right,K-i-1, vals)
                else:
                    find_val(node_path[i].left,K-i-1, vals)
            else:
                find_val(node_path[i],K-i, vals)
