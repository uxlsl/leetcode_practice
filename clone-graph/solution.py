# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

    def __repr__(self):
        return '<{}>'.format(self.val)

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # import copy
        # return copy.deepcopy(node)
        def f(node, visited):
            if node in visited:
                return visited[node]
            x = Node(node.val, [])
            visited[node] = x
            for i in node.neighbors:
                x.neighbors.append(f(i,visited))
            return x

        return f(node, {})
