from utils import TreeNode
from solution import Solution


def test_solution():
    s = Solution()
    tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    assert s.binaryTreePaths(tree) == ['1->2->5', '1->3']
