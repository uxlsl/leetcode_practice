# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        width = 1
        layer = [root]

        while any(layer):
            tmp = []
            width = max(width, len(layer))
            for i in layer:
                if i:
                    tmp.append(i.left)
                    tmp.append(i.right)
                else:
                    tmp.append(None)
                    tmp.append(None)
            if not any(tmp):
                break
            # 开掉左右二边的None
            for i in range(len(tmp)):
                if tmp[i] is not None:
                    start = i
                    break

            for i in reversed(range(len(tmp))):
                if tmp[i] is not None:
                    end = i
                    break

            layer = tmp[start:end+1]

        return width

