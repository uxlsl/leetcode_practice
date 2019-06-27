"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val or quadTree2.val, True, None, None, None, None)
        elif quadTree1.isLeaf and not quadTree2.isLeaf:
            # 可能要copy
            if quadTree1.val:
                return quadTree1
            else:
                return quadTree2

        elif not quadTree1.isLeaf and quadTree2.isLeaf:
            # 可能要copy
            if quadTree2.val:
                return quadTree2
            else:
                return quadTree1

        else:
            node = Node(
                None,
                False,
                self.intersect(quadTree1.topLeft, quadTree2.topLeft),
                self.intersect(quadTree1.topRight, quadTree2.topRight),
                self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft),
                self.intersect(quadTree1.bottomRight, quadTree2.bottomRight),
            )
            # 合并相同值的节点
            if (
                node.topLeft.isLeaf
                and node.topRight.isLeaf
                and node.bottomLeft.isLeaf
                and node.bottomRight.isLeaf
                and (
                    node.topLeft.val
                    == node.topRight.val
                    == node.bottomLeft.val
                    == node.bottomRight.val
                )
            ):
                node.isLeaf = True
                node.val = node.topLeft.val
                node.topLeft = None
                node.topRight = None
                node.bottomLeft = None
                node.bottomRight = None

            return node
