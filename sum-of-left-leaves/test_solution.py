from utils import TreeNode
from solution import Solution


def test_solution():
    tree = TreeNode(3, TreeNode(4), TreeNode(6))
    s = Solution()
    assert s.sumOfLeftLeaves(tree) == 4

