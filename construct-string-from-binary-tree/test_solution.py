from utils import TreeNode
from solution import Solution


def test_solution():
    s = Solution()
    tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    assert s.tree2str(tree) == 'xxx'
