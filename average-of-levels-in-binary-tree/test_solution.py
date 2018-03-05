from utils import TreeNode
from solution import Solution


def test_solution():
    s = Solution()
    tree = TreeNode(3,
            TreeNode(9),
                TreeNode(20, TreeNode(15), TreeNode(7)))
    assert s.averageOfLevels(tree) == [3, 14.5, 11]
