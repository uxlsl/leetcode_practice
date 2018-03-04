from utils import TreeNode, tree
from solution import Solution


def test_solution():
    s = Solution()
    #assert s.minDepth(tree) == 3

    tree = TreeNode(1, TreeNode(2))
    assert s.minDepth(tree) == 2
