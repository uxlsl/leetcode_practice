from utils import TreeNode
from solution import Solution


def test_solution():
    s = Solution()
    n = TreeNode(2)
    t = TreeNode(1, n)
    assert s.lowestCommonAncestor(t, t, n) == t
